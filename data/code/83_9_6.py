import datetime
def are_same_day(date1: datetime.datetime, date2: datetime.datetime) -> bool:
    return date1.date() == date2.date()
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 10, 26, 14, 30, 0)
    date_b = datetime.datetime(2023, 10, 26, 8, 0, 0)
    date_c = datetime.datetime(2023, 10, 27, 10, 0, 0)
    date_d = datetime.datetime(2023, 10, 26, 23, 59, 59)
    print(f"Date A and Date B are same day: {are_same_day(date_a, date_b)}")
    print(f"Date A and Date C are same day: {are_same_day(date_a, date_c)}")
    print(f"Date A and Date D are same day: {are_same_day(date_a, date_d)}")