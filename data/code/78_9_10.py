MONTHS_PER_YEAR = 12

def calculate_month_difference(month1: int, month2: int) -> int:
    return abs((month2 - month1 + MONTHS_PER_YEAR) % MONTHS_PER_YEAR)
if __name__ == '__main__':
    print(calculate_month_difference(5, 10))
    print(calculate_month_difference(10, 5))
    print(calculate_month_difference(12, 2))
    print(calculate_month_difference(-3, -9))
    print(calculate_month_difference(-12, -2))