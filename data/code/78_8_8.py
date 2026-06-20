def find_month_difference(month1: int, month2: int) -> int:
    return abs(month1 - month2)

if __name__ == '__main__':
    print(find_month_difference(1, 4))
    print(find_month_difference(12, 3))
    print(find_month_difference(6, 6))