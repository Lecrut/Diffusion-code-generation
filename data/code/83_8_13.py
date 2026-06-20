import datetime

def is_same_day(date1, date2):
    return date1.date() == date2.date()

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 14, 30)
    d2 = datetime.datetime(2023, 10, 26, 9, 45)
    d3 = datetime.datetime(2023, 11, 1, 18, 15)
    d4 = datetime.datetime(2023, 10, 25, 12, 0)

    print(f"Is {d1} on the same day as {d2}: {is_same_day(d1, d2)}")
    print(f"Is {d1} on the same day as {d3}: {is_same_day(d1, d3)}")
    print(f"Is {d3} on the same day as {d1}: {is_same_day(d3, d1)}")
    print(f"Is {d4} on the same day as {d1}: {is_same_day(d4, d1)}")