def get_day_of_month(timestamp):
    return timestamp % 30 + 1

if __name__ == '__main__':
    sample_timestamp = 28
    print(get_day_of_month(sample_timestamp))