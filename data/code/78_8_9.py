def validate_month_number(month: int) -> None:
    if not (1 <= month <= 12):
        raise ValueError("Month number must be between 1 and 12")

def find_month_difference(month1: int, month2: int) -> int:
    validate_month_number(month1)
    validate_month_number(month2)
    return abs(month1 - month2)

if __name__ == '__main__':
    print(find_month_difference(5, 10))
    print(find_month_difference(12, 3))
    print(find_month_difference(7, 7))