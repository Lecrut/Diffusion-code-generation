from datetime import date

def compare_dates(date1: date, date2: date) -> int:
    if date1 > date2:
        return 1
    elif date1 < date2:
        return -1
    else:
        return 0
if __name__ == '__main__':
    result = compare_dates(date(2023, 4, 1), date(2023, 3, 31))
    print(result)