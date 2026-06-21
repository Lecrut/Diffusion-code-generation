LEAP_RULES = {
    400: True,
    100: False,
    4: True,
    1: False
}

def is_leap_year(year):
    rules = [400, 100, 4, 1]
    for divisor in rules:
        if year % divisor == 0:
            return LEAP_RULES[divisor]
    return False

if __name__ == '__main__':
    samples = [2000, 1900, 2024, 2023, 2400, 1996, 2100, 2025]
    for year in samples:
        print(is_leap_year(year))