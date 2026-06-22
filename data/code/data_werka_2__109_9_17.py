from datetime import date

def get_remaining_days_in_month(start_date, end_date):
    if not isinstance(start_date, date):
        raise ValueError("start_date must be a date instance")
    if not isinstance(end_date, date):
        raise ValueError("end_date must be a date instance")
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    sample_start = date(2023, 10, 15)
    sample_end = date(2023, 10, 31)
    result = get_remaining_days_in_month(sample_start, sample_end)
    print(result)