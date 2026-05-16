from datetime import date
if __name__ == '__main__':
    d1 = date(2023, 10, 23)
    d2 = date(2023, 10, 28)
    print(d1.weekday() < 5)
    print(d2.weekday() < 5)