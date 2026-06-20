from datetime import date

def order_dates(date1: date, date2: date) -> tuple:
    return (date1, date2) if date1 < date2 else (date2, date1)

if __name__ == '__main__':
    d1 = date(2023, 1, 1)
    d2 = date(2022, 12, 31)
    print(order_dates(d1, d2))