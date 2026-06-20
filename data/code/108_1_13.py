def extract_day_from_timestamp(timestamp):
    year = timestamp // 10000
    month = (timestamp % 10000) // 100
    day = timestamp % 100
    return day

if __name__ == '__main__':
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {extract_day_from_timestamp(timestamp1)}")
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {extract_day_from_timestamp(timestamp2)}")
    timestamp3 = 20240229
    print(f"The day for {timestamp3} is: {extract_day_from_timestamp(timestamp3)}")