import datetime

def is_same_week(date_one: datetime.date, date_two: datetime.date) -> bool:
    if not isinstance(date_one, datetime.date):
        raise ValueError("First argument must be a date object")
    if not isinstance(date_two, datetime.date):
        raise ValueError("Second argument must be a date object")
    week_one = date_one.isocalendar()[1]
    year_one = date_one.isocalendar()[0]
    week_two = date_two.isocalendar()[1]
    year_two = date_two.isocalendar()[0]
    return year_one == year_two and week_one == week_two

if __name__ == '__main__':
    date_a = datetime.date(2024, 1, 1)
    date_b = datetime.date(2024, 1, 5)
    date_c = datetime.date(2024, 1, 8)
    print(is_same_week(date_a, date_b))
    print(is_same_week(date_a, date_c))