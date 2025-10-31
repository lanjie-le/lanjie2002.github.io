import tkinter as tk
import random
import threading
import time
import sys


def show_warm_tip():
    window_width = 300
    window_height = 150
    screen_width = 1920  # 请根据自己的屏幕分辨率修改
    screen_height = 1080  # 请根据自己的屏幕分辨率修改

    # 区域划分（4列3行），保持分布均匀
    region_cols = 4
    region_rows = 3
    col = random.randint(0, region_cols - 1)
    row = random.randint(0, region_rows - 1)
    x_min = col * (screen_width // region_cols)
    x_max = (col + 1) * (screen_width // region_cols) - window_width
    y_min = row * (screen_height // region_rows)
    y_max = (row + 1) * (screen_height // region_rows) - window_height
    x = random.randint(max(0, x_min), min(screen_width - window_width, x_max))
    y = random.randint(max(0, y_min), min(screen_height - window_height, y_max))

    window = tk.Tk()
    window.title('温馨提示')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tips = [
        '多喝水哦～', '保持微笑呀', '每天都要元气满满',
        '记得吃水果', '保持好心情', '好好爱自己', '我想你了',
        '梦想成真', '期待下一次见面', '金榜题名',
        '顺顺利利', '早点休息', '愿所有烦恼都消失',
        '别熬夜', '今天过得开心嘛', '天冷了，多穿衣服'
    ]
    tip = random.choice(tips)

    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]
    bg = random.choice(bg_colors)

    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=30,
        height=3
    ).pack()

    window.attributes('-topmost', True)
    # 窗口显示2秒后自动关闭
    window.after(2000, window.destroy)
    window.mainloop()


if __name__ == "__main__":
    total_running_time = 60  # 总运行时间（秒）
    interval = 0.005  # 弹出间隔时间（秒）
    
    start_time = time.time()
    threads = []
    
    try:
        while time.time() - start_time < total_running_time:
            # 创建并启动新线程
            t = threading.Thread(target=show_warm_tip)
            threads.append(t)
            t.start()
            # 等待指定间隔再创建下一个窗口
            time.sleep(interval)
        
        # 等待所有已创建的线程完成
        for t in threads:
            t.join()
            
        print("程序已运行1分钟，自动结束")
        sys.exit(0)
        
    except KeyboardInterrupt:
        print("程序被手动终止")
        sys.exit(0)