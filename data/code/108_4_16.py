import calendar

MAX_DAYS_IN_MONTH = 31
MIN_MONTH = 1
MAX_MONTH = 12

def validate_day_of_month(year, month, day):
    if not (MIN_MONTH <= month <= MAX_MONTH):
        raise ValueError("Month out of range")
    if not (1 <= day <= MAX_DAYS_IN_MONTH):
        raise ValueError("Day out of standard range")
    _, days_in_month = calendar.monthrange(year, month)
    if day > days_in_month:
        raise ValueError("Day exceeds month length")
    return day

if __name__ == '__main__':
    Y = 2024
    M = 2
    D = 29
    val = validate_day_of_month(Y, M, D)
    print(val)