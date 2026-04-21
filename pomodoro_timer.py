import time

def countdown(minutes, label):
    for second in range(minutes * 60, 0, -1):
        mins, secs = divmod(second, 60)
        timer = f"{label} - {mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
    print(f"{label} 完成！           ")

def pomodoro_timer():
    # 25 分鐘讀書
    countdown(25, "讀書中")
    # 5 分鐘休息
    countdown(5, "休息中")

if __name__ == "__main__":
    print("""
使用說明:
25 分鐘讀書，5 分鐘休息。循環開始！
按 Ctrl+C 可手動停止計時。
    """)
    try:
        while True:
            pomodoro_timer()
    except KeyboardInterrupt:
        print("\n番茄鐘計時器已停止，祝您讀書愉快！")
