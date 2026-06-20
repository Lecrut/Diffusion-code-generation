def find_month_difference(month1: int, month2: int) -> int:
    if not (1 <= month1 <= 12 and 1 <= month2 <= 12):
        raise ValueError('Month numbers must be between 1 and 12 inclusive.')
    return abs(month1 - month2)
if __name__ == '__main__':
    print(find_month_difference(5, 10))
    print(find_month_difference(12, 3))
    print(find_month_difference(7, 7))