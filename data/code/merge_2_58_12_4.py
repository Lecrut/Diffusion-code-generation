from datetime import date
def calculate_elapsed_days(start_date: date, end_date: date) -> int:
    if isinstance(start_date, type(end_date)) and not (isinstance(start_date, date) and isinstance(end_date, date)):
        raise TypeError("Both arguments must be instances of datetime.date.")
    if start_date > end_date:
        raise ValueError(f"start_date ({start_date}) cannot be greater than end_date ({end_date}).")
    return abs((end_date - start_date).days)
if __name__ == '__main__':
    sample_start = date(2023, 1, 15)
    sample_end = date(2023, 6, 20)
    days_difference = calculate_elapsed_days(sample_start, sample_end)
    print(f"Days between {sample_start} and {sample_end}: {days_difference}")