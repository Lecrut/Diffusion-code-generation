import calendar

def validate_day_of_month(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    max_days = calendar.monthrange(year, month)[1]
    if not (1 <= day <= max_days):
        raise ValueError("Invalid day for the given month")
    weekday_index = calendar.weekday(year, month, day)
    return {
        "year": year,
        "month": month,
        "day": day,
        "weekday": weekday_index
    }

if __name__ == '__main__':
    target_year = 1999
    target_month = 12
    target_day = 31
    validation_result = validate_day_of_month(target_year, target_month, target_day)
    print(validation_result)