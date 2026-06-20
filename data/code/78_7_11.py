def validate_month(month):
    if not isinstance(month, int) or month < 1 or month > 12:
        raise ValueError("Month must be an integer between 1 and 12")

def calculate_month_difference(month1, month2):
    validate_month(month1)
    validate_month(month2)
    return abs(month1 - month2)

if __name__ == '__main__':
    result = calculate_month_difference(3, 9)
    print(result)