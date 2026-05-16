import datetime
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 26)
    date2 = datetime.date(2023, 1, 1)
    if date1 > date2:
        print(f"{date1} is after {date2}")
    elif date1 < date2:
        print(f"{date1} is before {date2}")
    else:
        print(f"{date1} is the same as {date2}")