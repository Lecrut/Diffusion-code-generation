def is_leap_year(year):
    div_by_4 = (year & 3) == 0
    div_by_100 = (year % 100) == 0
    div_by_400 = (year % 400) == 0
    if not div_by_4:
        return False
    if not div_by_100:
        return True
    return div_by_400

if __name__ == '__main__':
    test_values = [2000, 1900, 2024, 2023, 2400, 1600, 1700, 2004, 2100, 400]
    for y in test_values:
        result = is_leap_year(y)
        print(f"{y} is leap: {result}")