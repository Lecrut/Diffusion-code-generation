def calculate_zeller_day(year, month, day):
    MONTH_ADJUSTMENT = 12
    YEAR_ADJUSTMENT = 1
    DIVISOR_CENTURY = 100
    MULTIPLIER_MONTH = 13
    DIVISOR_MONTH = 5
    MULTIPLIER_CENTURY_PART = 1
    DIVISOR_CENTURY_PART = 4
    MULTIPLIER_CENTURY = 2
    MODULUS = 7

    if month < 3:
        month += MONTH_ADJUSTMENT
        year -= YEAR_ADJUSTMENT

    k = year % DIVISOR_CENTURY
    j = year // DIVISOR_CENTURY
    q = day
    m = month

    h = (q + (MULTIPLIER_MONTH * (m + 1)) // DIVISOR_MONTH + k + (k // DIVISOR_CENTURY_PART) + (j // DIVISOR_CENTURY_PART) - (MULTIPLIER_CENTURY * j)) % MODULUS
    return h

if __name__ == '__main__':
    result = calculate_zeller_day(1900, 1, 1)
    print(result)