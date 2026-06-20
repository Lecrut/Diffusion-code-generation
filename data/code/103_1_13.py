import time

def calculate_milliseconds_since_midnight():
    now = time.time()
    start_of_day = time.mktime((now // 86400) * 86400)
    return int((now - start_of_day) * 1000)

if __name__ == '__main__':
    milliseconds = calculate_milliseconds_since_midnight()
    print(milliseconds)