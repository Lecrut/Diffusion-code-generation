def calculate_day_of_year(date_obj):
    is_leap_year = (date_obj.year % 4 == 0 and date_obj.year % 100 != 0) or date_obj.year % 400 == 0
    days_in_month = [31, 28 if not is_leap_year else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = sum(days_in_month[:date_obj.month - 1]) + date_obj.day
    return day_of_year

if __name__ == '__main__':
    sample_date = (2024, 2, 29)
    result = calculate_day_of_year(date(sample_date[0], sample_date[1], sample_date[2]))
    print(f"Date: {sample_date} -> Day of Year: {result}")