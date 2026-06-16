import datetime
def is_weekend(date_input):
    if isinstance(date_input, str):
        try:
            date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError:
            return False
    elif isinstance(date_input, datetime.date):
        date_obj = date_input
    else:
        return False
    day_of_week = date_obj.weekday()
    return day_of_week >= 5
if __name__ == '__main__':
    date1 = "2023-10-28"
    date2 = datetime.date(2023, 10, 29)
    date3 = "2023-10-29"
    date4 = datetime.date(2023, 10, 30)
    print(f"Is {date1} a weekend? {is_weekend(date1)}")
    print(f"Is {date2} a weekend? {is_weekend(date2)}")
    print(f"Is {date3} a weekend? {is_weekend(date3)}")
    print(f"Is {date4} a weekend? {is_weekend(date4)}")