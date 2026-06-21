import calendar

def validate_day(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    _, days_in_month = calendar.monthrange(year, month)
    if day > days_in_month:
        raise ValueError("Day is out of range for the given month")
    return day

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 29
    verified_day = validate_day(sample_year, sample_month, sample_day)
    print(verified_day)