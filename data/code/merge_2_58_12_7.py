from datetime import date
def calculate_elapsed_days(date_one: date, date_two: date) -> int:
    try:
        days_difference = date_two - date_one
        return abs(days_difference.days)
    except TypeError as e:
        raise ValueError(f"Both arguments must be datetime.date objects, got {type(date_one)} and {type(date_two)}.") from e
if __name__ == '__main__':
    sample_date_start = date(2023, 1, 5)
    sample_date_end = date(2024, 12, 25)
    elapsed_days = calculate_elapsed_days(sample_date_start, sample_date_end)
    print(f"Days between {sample_date_start} and {sample_date_end}: {elapsed_days}")