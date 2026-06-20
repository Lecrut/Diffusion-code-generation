from datetime import date

def days_between(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date_a = date(2023, 1, 1)
    date_b = date(2023, 1, 10)
    result = days_between(date_a, date_b)
    print(result)