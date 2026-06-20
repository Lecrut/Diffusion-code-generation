import time

def get_weekday(timestamp):
    return time.strftime('%A', time.localtime(timestamp))

if __name__ == '__main__':
    timestamp = int(time.mktime((2023, 1, 1, 0, 0, 0, 0, 0, 0)))
    print(get_weekday(timestamp))