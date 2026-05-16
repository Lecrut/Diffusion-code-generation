import datetime
def compare_dates(date1, date2):
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0
if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 26)
    d2 = datetime.date(2023, 10, 26)
    d3 = datetime.date(2023, 11, 1)
    d4 = datetime.date(2023, 10, 25)
    result1 = compare_dates(d1, d2)
    print(f"Comparing {d1} and {d2}: {result1}")
    result2 = compare_dates(d1, d3)
    print(f"Comparing {d1} and {d3}: {result2}")
    result3 = compare_dates(d4, d1)
    print(f"Comparing {d4} and {d1}: {result3}")
    result4 = compare_dates(d3, d4)
    print(f"Comparing {d3} and {d4}: {result4}")