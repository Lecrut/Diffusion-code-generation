def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return days_in_month[month - 1] + 1
    return days_in_month[month - 1]

def determine_day(timestamp):
    year = timestamp // 10000
    month = (timestamp % 10000) // 100
    day = timestamp % 100
    if day > get_days_in_month(year, month):
        raise ValueError("Invalid day for the given date")
    return day

if __name__ == '__main__':
    timestamp1 = 20231027
    print(f"The day for {timestamp1} is: {determine_day(timestamp1)}")
    timestamp2 = 19990101
    print(f"The day for {timestamp2} is: {determine_day(timestamp2)}")
    timestamp3 = 20240229
    print(f"The day for {timestamp3} is: {determine_day(timestamp3)}")