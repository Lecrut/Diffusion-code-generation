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
    print(compare_dates(d1, d2))
    d3 = date(2023, 1, 10)
    d4 = date(2023, 1, 1)
    print(compare_dates(d3, d4))
    d5 = date(2023, 5, 20)
    d6 = date(2023, 5, 20)
    print(compare_dates(d5, d6))