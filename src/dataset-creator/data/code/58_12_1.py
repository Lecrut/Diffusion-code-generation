from datetime import date
def calculate_elapsed_days(start_date: date, end_date: date) -> int:
    if isinstance(start_date, date) and isinstance(end_date, date):
        return abs((end_date - start_date).days)
    else:
        raise TypeError("Both arguments must be instances of datetime.date")
if __name__ == '__main__':
    sample_start = date(2023, 1, 15)
    sample_end = date(2024, 6, 20)
    elapsed_days = calculate_elapsed_days(sample_start, sample_end)
    print(f"Days between {sample_start} and {sample_end}: {elapsed_days}")