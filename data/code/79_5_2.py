import datetime
def get_next_month_first_day(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    new_date = datetime.datetime(next_year, next_month, 1)
    return new_date.strftime('%Y-%m-%d')
if __name__ == '__main__':
    sample_date1 = "2023-10-15"
    result1 = get_next_month_first_day(sample_date1)
    print(f"{sample_date1}: {result1}")
    sample_date2 = "2024-12-31"
    result2 = get_next_month_first_day(sample_date2)
    print(f"{sample_date2}: {result2}")
    sample_date3 = "2025-01-01"
    result3 = get_next_month_first_day(sample_date3)
    print(f"{sample_date3}: {result3}")