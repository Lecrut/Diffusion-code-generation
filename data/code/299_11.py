import datetime
def is_weekend(date_input):
    if isinstance(date_input, datetime.date):
        weekday = date_input.weekday()
    elif isinstance(date_input, str):
        try:
            date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            weekday = date_obj.weekday()
        except ValueError:
            return False
    else:
        return False
    return weekday >= 5
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 28)
    date2 = "2023-10-29"
    date3 = datetime.date(2023, 10, 30)
    date4 = "2023-10-31"
    date5 = "2023-11-01"
    print(f"Date {date1}: {is_weekend(date1)}")
    print(f"Date {date2}: {is_weekend(date2)}")
    print(f"Date {date3}: {is_weekend(date3)}")
    print(f"Date {date4}: {is_weekend(date4)}")
    print(f"Date {date5}: {is_weekend(date5)}")