from datetime import date

def validate_dates(start_date: date, end_date: date):
    if start_date > end_date:
        raise ValueError("Start date must be before end date.")

def years_between_dates(start_date: date, end_date: date) -> int:
    validate_dates(start_date, end_date)
    return (end_date.year - start_date.year) - ((start_date.month, start_date.day) > (end_date.month, end_date.day))

if __name__ == '__main__':
    start = date(2010, 5, 15)
    end = date(2023, 8, 20)
    print(years_between_dates(start, end))