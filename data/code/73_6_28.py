import datetime
import time

def date_difference(date1_str: str, date2_str: str) -> dict:
    fmt = "%Y-%m-%d"
    d1 = datetime.datetime.strptime(date1_str, fmt).date()
    d2 = datetime.datetime.strptime(date2_str, fmt).date()
    delta = d2 - d1
    days = delta.days
    sign = 1 if days >= 0 else -1
    abs_days = abs(days)
    return {
        "total_days": days,
        "years": abs_days // 365,
        "months": (abs_days % 365) // 30,
        "days": (abs_days % 365) % 30,
        "sign": sign
    }

if __name__ == '__main__':
    result = date_difference("2023-01-01", "2024-03-15")
    print(result)