from datetime import date

def dates_equal(date1: date, date2: date) -> bool:
    return date1 == date2

if __name__ == '__main__':
    sample_date1 = date(2023, 4, 15)
    sample_date2 = date(2023, 4, 15)
    print(dates_equal(sample_date1, sample_date2))