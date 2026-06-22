import datetime
import calendar

def get_month_status(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    if year < 1:
        raise ValueError(f"Invalid year: {year}")

    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    if year != current_year or month != current_month:
        raise ValueError("The specified month must be the current month.")

    days_in_month = calendar.monthrange(year, month)[1]
    days_passed = current_day
    days_remaining = days_in_month - current_day
    percentage_completed = (days_passed / days_in_month) * 100

    return {
        "year": year,
        "month": month,
        "days_remaining": days_remaining,
        "percentage_completed": percentage_completed
    }

if __name__ == '__main__':
    result = get_month_status(2023, 10)
    print(result)