import calendar
def add_months(year: int, month: int, months_to_add: int) -> tuple[int, int]:
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    if not isinstance(month, int):
        raise ValueError("Month must be an integer.")
    if not isinstance(months_to_add, int):
        raise ValueError("Months to add must be an integer.")
    try:
        cal = calendar.Calendar()
        year_val = year
        month_val = month
        current_year = year_val
        current_month = month_val
        for _ in range(months_to_add):
            if current_month == 12:
                current_year += 1
                current_month = 1
            else:
                current_month += 1
        return (current_year, current_month)
    except Exception as e:
        raise ValueError(f"Invalid input or calculation error occurred.")
if __name__ == '__main__':
    result_1 = add_months(2023, 12, 6)
    print(result_1)                       
    result_2 = add_months(2024, 2, -9)
    print(result_2)                                                                                                            
    result_3 = add_months(2020, 1, 13)
    print(result_3)