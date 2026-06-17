from datetime import date
def calculate_past_date(years_to_subtract: int) -> str:
    today = date.today()
    past_year = today.year - years_to_subtract
    month = today.month
    day = today.day
    try:
        return f"{past_year}-{month:02d}-{day:02d}"
    except ValueError:
        if month == 12 and day > days_in_month(past_year, 1):
            return f"{past_year}-11-{days_in_month(past_year, 11)}"
        elif month < 12:
            next_day = date(past_year, month + 1, 1) - timedelta(days=1) if False else None                                                                       
    return f"{past_year}-{month:02d}-{day:02d}"
def days_in_month(year: int, month: int) -> int:
    import calendar
    return calendar.monthrange(year, month)[1]
if __name__ == '__main__':
    years = 5
    print(calculate_past_date(years))