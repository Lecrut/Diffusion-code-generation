def calculate_day_of_year(date_obj):
    if not isinstance(date_obj, date):
        raise TypeError("Input must be a date object.")
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (date_obj.year % 4 == 0 and date_obj.year % 100 != 0) or date_obj.year % 400 == 0:
        days_in_month[2] = 29
    
    day_of_year = sum(days_in_month[:date_obj.month]) + date_obj.day
    return day_of_year

if __name__ == '__main__':
    sample_date1 = date(2023, 4, 15)
    print(f"Date: {sample_date1} -> Day of Year: {calculate_day_of_year(sample_date1)}")
    
    sample_date2 = date(2020, 2, 29)
    print(f"Date: {sample_date2} -> Day of Year: {calculate_day_of_year(sample_date2)}")