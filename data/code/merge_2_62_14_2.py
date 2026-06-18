import calendar
def add_months(year: int, month: int, months_to_add: int) -> tuple[int, int]:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    if months_to_add < 0:
        raise ValueError("Months to add must be non-negative.")
    current_year = year
    current_month = month + months_to_add
    while current_month > 12:
        current_month -= 12
        current_year += 1
    return (current_year, current_month)
if __name__ == '__main__':
    result_1 = add_months(2023, 5, 6)
    print(f"Adding 6 months to May 2023: {result_1}")
    result_2 = add_months(2023, 12, 1)
    print(f"Adding 1 month to December 2023: {result_2}")
    result_3 = add_months(2024, 2, 1)
    print(f"Adding 1 month to February 2024 (Leap Year): {result_3}" )