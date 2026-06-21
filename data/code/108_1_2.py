def get_day_of_month(timestamp):
    import time
    return time.localtime(timestamp).tm_mday

if __name__ == '__main__':
    print(get_day_of_month(1672531200))
    print(get_day_of_month(0))
    print(get_day_of_month(1609459200))