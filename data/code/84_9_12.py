def calculate_day_of_year(date_obj):
    if not isinstance(date_obj, date):
        raise TypeError("Input must be a date object.")
    
    is_leap_year = (date_obj.year % 4 == 0 and date_obj.year % 100 != 0) or date_obj.year % 400 == 0
    days_in_month = [31, 29 if is_leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day_of_year = sum(days_in_month[:date_obj.month - 1]) + date_obj.day
    return day_of_year

if __name__ == '__main__':
    from datetime import date
    
    sample_date = date(2023, 4, 15)
    print(f"Date: {sample_date} -> Day of Year: {calculate_day_of_year(sample_date)}")
    
    sample_date = date(2020, 2, 29)
    print(f"Date: {sample_date} -> Day of Year: {calculate_day_of_year(sample_date)}")