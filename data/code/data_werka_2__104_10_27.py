from datetime import date

def compare_dates(first: date, second: date) -> int:
    if first > second:
        return 1
    if first < second:
        return -1
    return 0

if __name__ == '__main__':
    later_date = date(2023, 12, 31)
    earlier_date = date(2023, 1, 1)
    result = compare_dates(later_date, earlier_date)
    print(result)