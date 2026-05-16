import datetime
def calculate_day_of_year(date_obj):
    year = date_obj.year
    if year % 400 == 0:
        is_leap = (year % 4 == 0)
    else:
        is_leap = (year % 4 == 0)
    days_in_year = 366 if is_leap else 365
    day_of_year = date_obj.timetuple().tm_yday
    return day_of_year
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 27)
    result1 = calculate_day_of_year(date1)
    print(f"Date: {date1}, Day of Year: {result1}")
    date2 = datetime.date(2000, 3, 1)
    result2 = calculate_day_of_year(date2)
    print(f"Date: {date2}, Day of Year: {result2}")
    date3 = datetime.date(2024, 2, 29)
    result3 = calculate_day_of_year(date3)
    print(f"Date: {date3}, Day of Year: {result3}")
    date4 = datetime.date(2023, 1, 1)
    result4 = calculate_day_of_year(date4)
    print(f"Date: {date4}, Day of Year: {result4}")