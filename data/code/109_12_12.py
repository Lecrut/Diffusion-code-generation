import datetime
import calendar

def get_month_progress(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be positive")

    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    if current_year != year or current_month != month:
        return {
            "year": year,
            "month": month,
            "total_days": calendar.monthrange(year, month)[1],
            "days_passed": 0,
            "days_remaining": 0,
            "percentage_complete": 0.0
        }

    total_days = calendar.monthrange(year, month)[1]
    days_passed = current_day
    days_remaining = total_days - current_day
    percentage_complete = (days_passed / total_days) * 100

    return {
        "year": year,
        "month": month,
        "total_days": total_days,
        "days_passed": days_passed,
        "days_remaining": days_remaining,
        "percentage_complete": round(percentage_complete, 2)
    }

if __name__ == '__main__':
    result = get_month_progress(2023, 10)
    print(result)