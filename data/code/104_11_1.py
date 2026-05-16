import datetime
def compare_dates(date1, date2):
    if date1 < date2:
        return (date1, date2)
    elif date2 < date1:
        return (date2, date1)
    else:
        return (date1, date2)
if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    d2 = datetime.datetime(2023, 10, 25, 15, 0, 0)
    d3 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    d4 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    print(compare_dates(d1, d2))
    print(compare_dates(d3, d4))
    print(compare_dates(d2, d1))
    print(compare_dates(d4, d3))
    print(compare_dates(d1, d1))