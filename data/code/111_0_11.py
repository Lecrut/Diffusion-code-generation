from datetime import date

def validate_date_range(start_date, end_date):
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Inputs must be date objects")
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")

def calculate_days(start_date, end_date):
    validate_date_range(start_date, end_date)
    return (end_date - start_date).days

if __name__ == '__main__':
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)
    days = calculate_days(start_date, end_date)
    print(days)