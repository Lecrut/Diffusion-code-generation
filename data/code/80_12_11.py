from datetime import date

def order_dates(date1: date, date2: date) -> tuple:
    return (date1, date2) if date1 < date2 else (date2, date1)

if __name__ == '__main__':
    sample_date1 = date(2023, 4, 1)
    sample_date2 = date(2023, 3, 15)
    ordered_dates = order_dates(sample_date1, sample_date2)
    print(ordered_dates)