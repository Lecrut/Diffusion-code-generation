def calculate_day_of_month(timestamp):
    year = timestamp // 10000
    month = (timestamp % 10000) // 100
    day = timestamp % 100
    
    if month == 2:
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return day + is_leap_year
    elif month in [4, 6, 9, 11]:
        return day + 30
    else:
        return day

if __name__ == '__main__':
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {calculate_day_of_month(timestamp1)}")
    
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {calculate_day_of_month(timestamp2)}")
    
    timestamp3 = 20240229
    print(f"The day for {timestamp3} is: {calculate_day_of_month(timestamp3)}")