import datetime
lambda dt:dt.day
if __name__ == '__main__':
    now = datetime.datetime(2023, 10, 27, 14, 30, 0)
    result = (lambda dt:dt.day)(now)
    print(result)