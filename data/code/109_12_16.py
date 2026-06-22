import datetime
import calendar

def get_month_status(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be positive")

    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    if year != current_year or month != current_month:
        raise ValueError("Year and month must match the current date")

    days_in_month = calendar.monthrange(year, month)[1]
    days_passed = current_day
    days_remaining = days_in_month - current_day
    percentage_complete = (days_passed / days_in_month) * 100

    return {
        "year": year,
        "month": month,
        "days_in_month": days_in_month,
        "days_passed": days_passed,
        "days_remaining": days_remaining,
        "percentage_complete": percentage_complete
    }

if __name__ == '__main__':
    now = datetime.date.today()
    result = get_month_status(now.year, now.month)
    print(result)