def get_day_of_month(timestamp):
    return timestamp // 86400 % 31 + 1
if __name__ == '__main__':
    print(get_day_of_month(1672531200))