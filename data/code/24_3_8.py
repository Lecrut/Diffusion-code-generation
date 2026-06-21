DIVISOR_RULES = {
    400: True,
    100: False,
    4: True
}

def is_leap_year(year):
    for divisor, expected in DIVISOR_RULES.items():
        if year % divisor == 0:
            return expected
    return False

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))