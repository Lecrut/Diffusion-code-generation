import calendar

MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

def validate_day(year, month, day):
    if not (MIN_MONTH <= month <= MAX_MONTH):
        raise ValueError("Month out of range")
    if not (MIN_DAY <= day <= MAX_DAY):
        raise ValueError("Day out of range")
    _, days_in_month = calendar.monthrange(year, month)
    if day > days_in_month:
        raise ValueError("Day exceeds month length")
    return day

if __name__ == '__main__':
    y = 2024
    m = 2
    d = 29
    val = validate_day(y, m, d)
    print(val)