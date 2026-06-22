from datetime import date

def days_between(d1: date, d2: date) -> int:
    delta = d2 - d1
    return delta.days

if __name__ == '__main__':
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 10)
    result = days_between(date1, date2)
    print(result)