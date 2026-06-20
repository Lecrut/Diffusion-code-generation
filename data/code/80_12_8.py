from datetime import date

def order_dates(date1: date, date2: date) -> tuple[date, date]:
    return (date1, date2) if date1 < date2 else (date2, date1)

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 15)
    sample_date2 = date(2023, 1, 10)
    print(order_dates(sample_date1, sample_date2))