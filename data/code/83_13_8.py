from datetime import date

def are_dates_same(date1: date, date2: date) -> bool:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise TypeError('Both arguments must be instances of the date class')
    return date1 == date2

if __name__ == '__main__':
    try:
        sample_date1 = date(2024, 3, 15)
        sample_date2 = date(2024, 3, 15)
        sample_date3 = date(2024, 3, 16)

        print(f"Are {sample_date1} and {sample_date2} the same? {are_dates_same(sample_date1, sample_date2)}")
        print(f"Are {sample_date1} and {sample_date3} the same? {are_dates_same(sample_date1, sample_date3)}")
    except TypeError as e:
        print(e)