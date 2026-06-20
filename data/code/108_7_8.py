def get_day_of_month(timestamp):
    return timestamp // 86400 % 30 + 1
if __name__ == '__main__':
    sample_timestamp = 1633072800
    print(get_day_of_month(sample_timestamp))