from datetime import date

def is_weekend(day):
    return day.weekday() >= 5

if __name__ == '__main__':
    d1 = date(2023, 10, 29)
    d2 = date(2023, 10, 30)
    print(is_weekend(d1))
    print(is_weekend(d2))