from datetime import date

def order_dates(date1, date2):
    return (date1, date2) if date1 < date2 else (date2, date1)

if __name__ == '__main__':
    print(order_dates(date(2023, 1, 1), date(2023, 1, 15)))