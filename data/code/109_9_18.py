from datetime import date

_MONTH_DAYS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def remaining_days_in_current_month():
    current = date(2023, 10, 15)
    month_days = _MONTH_DAYS[current.month]
    total_days_in_month = month_days
    days_passed = current.day
    remaining = total_days_in_month - days_passed
    return remaining

if __name__ == '__main__':
    result = remaining_days_in_current_month()
    print(result)