def days_in_month(year, month):
    if month == 2:
        return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def seconds_left_in_month(timestamp):
    current_time = timestamp
    current_year = current_time // 31536000 + 1970
    current_month = current_time % 31536000 // 2628000 + 1
    days_passed = current_time % 2628000 // 86400
    seconds_in_day = 86400
    remaining_days = days_in_month(current_year, current_month) - days_passed
    return remaining_days * seconds_in_day
if __name__ == '__main__':
    sample_timestamp = 1672531200
    print(seconds_left_in_month(sample_timestamp))