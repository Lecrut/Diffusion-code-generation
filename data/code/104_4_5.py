from datetime import date

def is_same_date(date1: tuple, date2: tuple) -> bool:
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    return date(y1, m1, d1) == date(y2, m2, d2)

if __name__ == '__main__':
    result = is_same_date((2023, 10, 5), (2023, 10, 5))
    print(result)