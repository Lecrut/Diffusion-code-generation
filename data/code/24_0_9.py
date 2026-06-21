DIVISIBILITY_MAP = {
    400: 1,
    100: 2,
    4: 3
}

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    test_cases = [2400, 2000, 1900, 1800, 2024, 2025]
    for y in test_cases:
        print(is_leap_year(y))