import datetime
def manipulate_date_components(date_obj):
    if date_obj.month == 12:
        new_month = 1
        new_year = date_obj.year + 1
    else:
        new_month = date_obj.month + 1
        new_year = date_obj.year
    return datetime.date(new_year, new_month, date_obj.day)
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 15)
    result1 = manipulate_date_components(date1)
    print(f"Original: {date1}, Result: {result1}")
    date2 = datetime.date(2023, 12, 25)
    result2 = manipulate_date_components(date2)
    print(f"Original: {date2}, Result: {result2}")
    date3 = datetime.date(2024, 1, 5)
    result3 = manipulate_date_components(date3)
    print(f"Original: {date3}, Result: {result3}")