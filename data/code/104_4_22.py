from datetime import date

def is_same_date(date1: tuple, date2: tuple) -> bool:
    d1 = date(date1[0], date1[1], date1[2])
    d2 = date(date2[0], date2[1], date2[2])
    return d1 == d2

if __name__ == '__main__':
    result = is_same_date((2023, 10, 5), (2023, 10, 5))
    print(result)