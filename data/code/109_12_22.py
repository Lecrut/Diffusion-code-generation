import datetime
import calendar

def get_month_status(year: int, month: int) -> dict:
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    if year < 1:
        raise ValueError(f"Invalid year: {year}")

    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])
    today = datetime.date.today()

    total_days = (last_day - first_day).days + 1
    days_elapsed = (today - first_day).days + 1

    if days_elapsed < 1:
        days_elapsed = 1
    if days_elapsed > total_days:
        days_elapsed = total_days

    remaining_days = total_days - days_elapsed
    percentage = (days_elapsed / total_days) * 100

    return {
        "year": year,
        "month": month,
        "total_days": total_days,
        "days_elapsed": days_elapsed,
        "remaining_days": remaining_days,
        "percentage": percentage
    }

if __name__ == '__main__':
    result = get_month_status(2023, 10)
    print(result)