from datetime import date

def are_dates_equal(d1: date, d2: date) -> bool:
    return d1 == d2

if __name__ == '__main__':
    sample_date1 = date(2023, 10, 5)
    sample_date2 = date(2023, 10, 5)
    print(are_dates_equal(sample_date1, sample_date2))