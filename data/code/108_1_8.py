def determine_day(timestamp):
    if not isinstance(timestamp, int) or timestamp < 1000000:
        raise ValueError("Invalid timestamp format")
    
    year = timestamp // 10000
    month = (timestamp % 10000) // 100
    day = timestamp % 100
    
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    
    return day

if __name__ == '__main__':
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {determine_day(timestamp1)}")
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {determine_day(timestamp2)}")
    timestamp3 = 20240229
    try:
        print(f"The day for {timestamp3} is: {determine_day(timestamp3)}")
    except ValueError as e:
        print(e)