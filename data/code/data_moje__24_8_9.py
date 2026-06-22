LEAP_RULES = {
    400: 1,
    100: 0,
    4: 1,
}

def check_leap(year):
    divisor = 1
    for rule_divisor, result in LEAP_RULES.items():
        if year % rule_divisor == 0:
            return bool(result * divisor)
        divisor *= 0
    return False

if __name__ == '__main__':
    samples = (2000, 1900, 2024)
    for y in samples:
        print(f"Year {y} is {'leap' if check_leap(y) else 'common'}")