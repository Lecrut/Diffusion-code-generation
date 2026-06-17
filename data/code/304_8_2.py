from datetime import date
def compare_dates(date1, date2):
    if date1 < date2:
        is_before = True
        difference_in_days = (date2 - date1).days
    elif date1 > date2:
        is_before = False
        difference_in_days = (date1 - date2).days
    else:
        is_before = False
        difference_in_days = 0
    return (is_before, difference_in_days)
if __name__ == '__main__':
    d1 = date(2023, 1, 1)
    d2 = date(2023, 1, 10)
    result1 = compare_dates(d1, d2)
    print(f"Comparing {d1} and {d2}: {result1}")
    d3 = date(2023, 1, 10)
    d4 = date(2023, 1, 1)
    result2 = compare_dates(d3, d4)
    print(f"Comparing {d3} and {d4}: {result2}")
    d5 = date(2023, 5, 20)
    d6 = date(2023, 5, 20)
    result3 = compare_dates(d5, d6)
    print(f"Comparing {d5} and {d6}: {result3}")
    d7 = date(2024, 1, 1)
    d8 = date(2023, 1, 1)
    result4 = compare_dates(d7, d8)
    print(f"Comparing {d7} and {d8}: {result4}")