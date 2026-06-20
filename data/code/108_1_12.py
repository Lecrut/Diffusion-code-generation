def get_day_of_month(timestamp):
    year = timestamp // 10000
    month = (timestamp % 10000) // 100
    day = timestamp % 100
    return day

if __name__ == '__main__':
    sample_timestamp1 = 20231027
    print(f"The day for {sample_timestamp1} is: {get_day_of_month(sample_timestamp1)}")
    sample_timestamp2 = 19990101
    print(f"The day for {sample_timestamp2} is: {get_day_of_month(sample_timestamp2)}")
    sample_timestamp3 = 20240229
    print(f"The day for {sample_timestamp3} is: {get_day_of_month(sample_timestamp3)}")