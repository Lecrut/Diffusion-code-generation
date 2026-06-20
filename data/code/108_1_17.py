def determine_day(timestamp):
    year = timestamp // 10000
    month = timestamp % 10000 // 100
    day = timestamp % 100
    is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    days_in_month = [31, 28 + int(is_leap_year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day
if __name__ == '__main__':
    timestamp1 = 20231027
    print(f'The day for {timestamp1} is: {determine_day(timestamp1)}')
    timestamp2 = 19990101
    print(f'The day for {timestamp2} is: {determine_day(timestamp2)}')
    timestamp3 = 20240229
    print(f'The day for {timestamp3} is: {determine_day(timestamp3)}')