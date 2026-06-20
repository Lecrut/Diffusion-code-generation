from datetime import date

def are_dates_same(date1: date, date2: date) -> bool:
    return date1 == date2
if __name__ == '__main__':
    sample_date1 = date(2023, 10, 5)
    sample_date2 = date(2023, 10, 5)
    sample_date3 = date(2023, 10, 6)
    print(are_dates_same(sample_date1, sample_date2))
    print(are_dates_same(sample_date1, sample_date3))