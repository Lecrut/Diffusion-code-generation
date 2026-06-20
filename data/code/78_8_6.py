def validate_month(month):
    if not isinstance(month, int) or month < 1 or month > 12:
        raise ValueError("Month must be an integer between 1 and 12")

def find_month_difference(month1: int, month2: int) -> int:
    validate_month(month1)
    validate_month(month2)
    return abs(month1 - month2)

if __name__ == '__main__':
    print(find_month_difference(5, 10))
    print(find_month_difference(12, 3))
    print(find_month_difference(7, 7))