from datetime import date

def compare_dates(first: date, second: date) -> int:
    if first > second:
        return 1
    if first < second:
        return -1
    return 0

if __name__ == '__main__':
    d1 = date(2023, 10, 15)
    d2 = date(2023, 10, 10)
    result = compare_dates(d1, d2)
    print(result)
    d3 = date(2023, 10, 10)
    result2 = compare_dates(d1, d3)
    print(result2)
    d4 = date(2023, 10, 15)
    result3 = compare_dates(d1, d4)
    print(result3)