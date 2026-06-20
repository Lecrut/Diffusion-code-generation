from datetime import date

def are_dates_identical(date1: date, date2: date) -> bool:
    return date1 == date2
if __name__ == '__main__':
    print(are_dates_identical(date(2023, 4, 1), date(2023, 4, 1)))
    print(are_dates_identical(date(2023, 4, 1), date(2023, 4, 2)))