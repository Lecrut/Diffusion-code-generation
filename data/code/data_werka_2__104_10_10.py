from datetime import date

def compare_dates(first_date: date, second_date: date) -> int:
    if first_date > second_date:
        return 1
    if first_date < second_date:
        return -1
    return 0

if __name__ == '__main__':
    d1 = date(2023, 10, 15)
    d2 = date(2023, 10, 10)
    result = compare_dates(d1, d2)
    print(result)