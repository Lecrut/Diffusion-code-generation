MONTHS_PER_YEAR = 12

def find_month_difference(month1: int, month2: int) -> int:
    return abs((month2 - month1) % MONTHS_PER_YEAR)

if __name__ == '__main__':
    print(find_month_difference(5, 10))
    print(find_month_difference(12, 3))
    print(find_month_difference(7, 7))