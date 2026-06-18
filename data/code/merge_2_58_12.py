from datetime import date
def calculate_elapsed_days(start_date: date, end_date: date) -> int:
    if start_date is None or end_date is None:
        raise ValueError("Both arguments must be non-None datetime.date objects.")
    return abs((end_date - start_date).days)
if __name__ == '__main__':
    sample_start = date(2023, 1, 15)
    sample_end = date(2024, 6, 20)
    result_days = calculate_elapsed_days(sample_start, sample_end)
    print(f"Elapsed days: {result_days}")