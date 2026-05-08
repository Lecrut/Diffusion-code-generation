import datetime
def manipulate_date(date_obj):
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    new_year = year + 1
    new_month = month + 1
    new_day = day - 5
    return datetime.date(new_year, new_month, new_day)
if __name__ == '__main__':
    initial_date = datetime.date(2023, 10, 25)
    print(f"Initial Date: {initial_date}")
    manipulated_date = manipulate_date(initial_date)
    print(f"Manipulated Date: {manipulated_date}")