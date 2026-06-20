def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if is_leap_year(year) else 28

def calculate_day_of_year(date_obj):
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    
    if not (1 <= month <= 12 and 1 <= day <= days_in_month(year, month)):
        raise ValueError("Invalid date")
    
    day_of_year = sum(days_in_month(year, m) for m in range(1, month)) + day
    return day_of_year

if __name__ == '__main__':
    sample_date = (2023, 4, 15)
    result1 = calculate_day_of_year(date(sample_date[0], sample_date[1], sample_date[2]))
    print(f"Date: {sample_date} -> Day of Year: {result1}")
    
    sample_date = (2020, 2, 29)
    result2 = calculate_day_of_year(date(sample_date[0], sample_date[1], sample_date[2]))
    print(f"Date: {sample_date} -> Day of Year: {result2}")