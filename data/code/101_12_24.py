def get_zeller_weekday(year, month, day):
    MONTH_OFFSET = 1
    CENTURY_DIVISOR = 100
    WEEKDAY_CYCLE = 7
    SUNDAY_INDEX = 1
    SATURDAY_INDEX = 0
    if month < 3:
        month += 12
        year -= 1
    k = year % CENTURY_DIVISOR
    j = year // CENTURY_DIVISOR
    h = (day + (13 * (month + MONTH_OFFSET)) // 5 + k + k // 4 + j // 4 - 2 * j) % WEEKDAY_CYCLE
    return h
if __name__ == '__main__':
    result = get_zeller_weekday(1900, 1, 1)
    print(result)