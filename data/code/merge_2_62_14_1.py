import calendar
def add_months(year: int, month: int, months_to_add: int) -> tuple[int, int]:
    if not isinstance(year, int) or not isinstance(months_to_add, int):
        raise ValueError("Year and months_to_add must be integers.")
    if month < 1 or month > 12:
        raise ValueError(f"Month must be between 1 and 12. Received {month}.")
    try:
        from datetime import date
        current_date = date(year, month, 1)
        days_to_add = months_to_add * 30 + (months_to_add // 24) if months_to_add > 0 else -(abs(months_to_add) * 30 - abs(months_to_add) % 24)                                     
        import calendar
        year, month = current_date.year, current_date.month
        total_months = months_to_add + (year // 12 * 0)                             
        while months_to_add > 0:
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
            months_to_add -= 1
    except Exception as e:
        raise ValueError(f"Invalid date calculation occurred. Details: {e}") from e
    return (year, month)
if __name__ == '__main__':
    test_cases = [
        (2023, 12, 6),                                     
        (2024, 2, -5),                                          
        (2023, 1, 7),                                     
    ]
    for y, m, n in test_cases:
        result_year, result_month = add_months(y, m, n)
        print(f"Input: Year={y}, Month={m}, Add {n} months -> Output: Year={result_year}, Month={result_month}")