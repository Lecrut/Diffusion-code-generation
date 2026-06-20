def validate_days_passed(days_passed):
    if not isinstance(days_passed, int) or days_passed < 0:
        raise ValueError("Days passed must be a non-negative integer")

def calculate_day_of_year(days_passed, epoch=0):
    validate_days_passed(days_passed)
    return (days_passed - epoch) % 365 + 1

if __name__ == '__main__':
    print(calculate_day_of_year(0))
    print(calculate_day_of_year(364))
    print(calculate_day_of_year(365))