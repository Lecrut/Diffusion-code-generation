from datetime import date
import calendar

DAY_UNITS = {
    "week": 7,
    "fortnight": 14,
    "month_avg": 30,
    "year": 365
}

def compute_date_delta(start: date, end: date) -> int:
    if not isinstance(start, date) or not isinstance(end, date):
        raise ValueError("Arguments must be date objects")
    delta = end - start
    return delta.days

def format_delta_with_context(days: int) -> dict:
    weeks = days // DAY_UNITS["week"]
    remaining_days = days % DAY_UNITS["week"]
    return {
        "total_days": days,
        "weeks": weeks,
        "remaining_days": remaining_days
    }

if __name__ == '__main__':
    d1 = date(2023, 11, 1)
    d2 = date(2023, 12, 15)
    raw_days = compute_date_delta(d1, d2)
    context = format_delta_with_context(raw_days)
    print(context["total_days"])
    print(context["weeks"])
    print(context["remaining_days"])