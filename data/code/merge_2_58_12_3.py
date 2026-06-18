from datetime import date
def calculate_elapsed_days(start_date: date, end_date: date) -> int:
    delta = end_date - start_date
    return abs(delta.days)
if __name__ == '__main__':
    sample_start = date(2023, 1, 15)
    sample_end = date(2023, 4, 15)
    result_days = calculate_elapsed_days(sample_start, sample_end)
    print(f"Days between {sample_start} and {sample_end}: {result_days}")