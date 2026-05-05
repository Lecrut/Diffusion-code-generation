import datetime
def are_same_day(date1: datetime.datetime, date2: datetime.datetime) -> bool:
    return date1.date() == date2.date()
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 10, 26, 14, 30, 0)
    date_b = datetime.datetime(2023, 10, 26, 9, 0, 0)
    date_c = datetime.datetime(2023, 10, 27, 10, 0, 0)
    date_d = datetime.datetime(2023, 10, 26, 23, 59, 59)
    print(f"A and B same day: {are_same_day(date_a, date_b)}")
    print(f"A and C same day: {are_same_day(date_a, date_c)}")
    print(f"A and D same day: {are_same_day(date_a, date_d)}")
    print(f"B and C same day: {are_same_day(date_b, date_c)}")