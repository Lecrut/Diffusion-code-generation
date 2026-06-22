import calendar

def validate_date_components(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month out of range")
    max_days = calendar.monthrange(year, month)[1]
    if not (1 <= day <= max_days):
        raise ValueError("Day out of range")
    return day

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    computed_day = validate_date_components(target_year, target_month, target_day)
    print(computed_day)