from datetime import date

def compare_dates(date1: date, date2: date) -> int:
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0
if __name__ == '__main__':
    date_a = date(2023, 10, 5)
    date_b = date(2023, 10, 15)
    result = compare_dates(date_a, date_b)
    print(result)