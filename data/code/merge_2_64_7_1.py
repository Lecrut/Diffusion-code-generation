import calendar as cal
def validate_date(year: int, month: int, day: int) -> bool:
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        if not (1 <= year <= 9999):
            return False
        cal.Calendar().setyear(year)
        max_day = cal.monthrange(year, month)[1]
        if not (1 <= month <= 12):
            return False
        if not (1 <= day <= max_day):
            return False
    except ValueError:
        return False
    return True
def generate_date_string(year: int = None, month: str = None, day: int = None) -> tuple[bool, str]:
    if year is not None or (month is not None and isinstance(month, str)):
        try:
            y = int(year) if year else 2023
            m = cal.month_name(int(month)) if month else "January"
            d_str = day if day else 15
            date_obj = cal.Calendar().setyear(y).month(m, d_str)
        except (ValueError, TypeError):
            return False, f"Invalid input: Year={year}, Month={month}, Day={day}"
    elif year is None and month is None and day is None:
        y = 2023
        m = "January"
        d_str = 15
        date_obj = cal.Calendar().setyear(y).month(m, d_str)
    else:
        return False, f"Invalid input combination provided."
    if not validate_date(year or y, month or str(m), day or int(d_str)):
        return False, "Date validation failed."
    formatted = cal.Calendar().setyear(y).month(m, d_str)
    result_string = f"{formatted.year} {m} {d_str}"
    return True, result_string
if __name__ == '__main__':
    success, output = generate_date_string(year=2023, month="March", day=15)
    print(output if success else "Validation Error")