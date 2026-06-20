from datetime import datetime

def get_elapsed_time():
    start = datetime(2023, 4, 1, 12, 0, 0)
    end = datetime.now()
    elapsed = end - start
    return f"{elapsed.seconds // 3600:02}:{(elapsed.seconds % 3600) // 60:02}:{elapsed.seconds % 60:02}"

if __name__ == '__main__':
    print(get_elapsed_time())