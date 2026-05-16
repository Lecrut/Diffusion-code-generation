import datetime
def get_next_month_date(date_obj):
    year = date_obj.year
    month = date_obj.month
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    return datetime.date(next_year, next_month, 1)
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 15)
    result1 = get_next_month_date(date1)
    print(f"Next month after {date1}: {result1}")
    date2 = datetime.date(2024, 12, 31)
    result2 = get_next_month_date(date2)
    print(f"Next month after {date2}: {result2}")
    date3 = datetime.date(2025, 1, 5)
    result3 = get_next_month_date(date3)
    print(f"Next month after {date3}: {result3}")