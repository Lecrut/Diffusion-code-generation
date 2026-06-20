from datetime import date

def order_dates(date1: date, date2: date) -> tuple:
    return (date1, date2) if date1 < date2 else (date2, date1)

if __name__ == '__main__':
    date_a = date(2023, 4, 15)
    date_b = date(2023, 3, 20)
    print(order_dates(date_a, date_b))