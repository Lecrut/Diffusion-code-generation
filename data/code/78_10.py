def find_month_difference(month1: int, month2: int) -> int:
    return abs(month1 - month2)
if __name__ == '__main__':
    m1 = 10
    m2 = 3
    difference = find_month_difference(m1, m2)
    print(difference)