import time
import os

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end='\r')  # 在同一行上更新计时器显示
        time.sleep(1)
        seconds -= 1

    print("\n专注时间结束！")

# 设置专注时长（以分钟为单位）
focus_time_minutes = 25

# 清屏（适用于终端或命令提示符）
os.system('cls' if os.name == 'nt' else 'clear')

# 启动专注时钟
focus_timer(focus_time_minutes)
