def categorize_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    if value < 0:
        raise ValueError("Input must be non-negative")
    if value < 10:
        return 'low'
    if value < 50:
        return 'medium'
    return 'high'

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(25))
    print(categorize_number(75))
    print(categorize_number(9))
    print(categorize_number(50))
    print(categorize_number(100))