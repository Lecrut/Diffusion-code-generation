DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def calculate_day_of_year(date_obj):
    month, day = date_obj.month, date_obj.day
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    if day < 1 or day > DAYS_IN_MONTH[month - 1]:
        raise ValueError("Day must be valid for the given month.")
    
    days_in_year = sum(DAYS_IN_MONTH)
    if is_leap_year(date_obj.year):
        days_in_year += 1
    
    day_of_year = sum(DAYS_IN_MONTH[:month-1]) + day
    return day_of_year

if __name__ == '__main__':
    sample_date = (2023, 4, 15)
    date_obj = date(sample_date[0], sample_date[1], sample_date[2])
    print(f"Date: {sample_date} -> Day of Year: {calculate_day_of_year(date_obj)}")