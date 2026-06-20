def extract_day_of_month(timestamp):
    SECONDS_PER_DAY = 86400
    return timestamp % SECONDS_PER_DAY // 3600
if __name__ == '__main__':
    timestamp1 = 1702531200
    print(extract_day_of_month(timestamp1))