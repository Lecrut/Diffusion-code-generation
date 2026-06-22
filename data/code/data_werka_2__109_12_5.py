import datetime
import calendar

def get_month_progress(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be positive")

    today = datetime.date.today()
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])

    if today < first_day:
        total_days = calendar.monthrange(year, month)[1]
        remaining_days = total_days
        days_passed = 0
    elif today > last_day:
        total_days = calendar.monthrange(year, month)[1]
        remaining_days = 0
        days_passed = total_days
    else:
        total_days = calendar.monthrange(year, month)[1]
        days_passed = (today - first_day).days + 1
        remaining_days = total_days - days_passed + 1

    percentage = (days_passed / total_days) * 100 if total_days > 0 else 0.0

    return {
        "year": year,
        "month": month,
        "total_days": total_days,
        "days_passed": days_passed,
        "remaining_days": remaining_days,
        "percentage_completed": round(percentage, 2)
    }

if __name__ == '__main__':
    result = get_month_progress(2023, 10)
    print(result)