def validate_month(month: int) -> bool:
    return 1 <= month <= 12

def calculate_month_difference(start_month: int, end_month: int) -> int:
    if not (validate_month(start_month) and validate_month(end_month)):
        raise ValueError('Month values must be between 1 and 12')
    return abs(end_month - start_month)
if __name__ == '__main__':
    print(calculate_month_difference(5, 10))
    print(calculate_month_difference(10, 5))
    print(calculate_month_difference(12, 2))
    print(calculate_month_difference(2, 12))
    print(calculate_month_difference(-3, -9))