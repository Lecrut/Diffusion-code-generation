from datetime import date
def calculate_elapsed_days(date_a: date, date_b: date) -> int:
    if not isinstance(date_a, date) or not isinstance(date_b, date):
        raise TypeError("Both arguments must be instances of datetime.date.")
    return abs((date_b - date_a).days)
if __name__ == '__main__':
    sample_date_1 = date(2023, 5, 17)
    sample_date_2 = date(2024, 8, 9)
    result_days = calculate_elapsed_days(sample_date_1, sample_date_2)
    print(f"Elapsed days between {sample_date_1} and {sample_date_2}: {result_days}")