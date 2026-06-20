MONTHS_PER_YEAR = 12

def find_month_difference(month1: int, month2: int) -> int:
    return abs(month1 - month2)
if __name__ == '__main__':
    month_a = 5
    month_b = 10
    month_c = 3
    month_d = 7
    print(f'Difference between {month_a} and {month_b}: {find_month_difference(month_a, month_b)}')
    print(f'Difference between {month_c} and {month_d}: {find_month_difference(month_c, month_d)}')