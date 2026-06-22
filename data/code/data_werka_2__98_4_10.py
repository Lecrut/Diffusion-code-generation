def _validate_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")
    if value != value:
        raise ValueError("NaN is not a valid input")

def categorize_number(value):
    _validate_number(value)
    if value < 10:
        return 'low'
    if value < 50:
        return 'medium'
    return 'high'

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(35))
    print(categorize_number(100))
    print(categorize_number(-1))
    print(categorize_number(49))
    print(categorize_number(50))