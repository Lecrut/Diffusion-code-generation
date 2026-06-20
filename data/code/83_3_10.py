from datetime import date

def check_date_equality(d1: date, d2: date) -> bool:
    return d1 == d2

if __name__ == '__main__':
    date_a = date(2023, 10, 26)
    date_b = date(2023, 10, 26)
    result1 = check_date_equality(date_a, date_b)
    print(result1)