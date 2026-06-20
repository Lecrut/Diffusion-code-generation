def get_day_of_month(timestamp):
    return timestamp // 86400 % 30 + 1
if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(get_day_of_month(sample_timestamp))