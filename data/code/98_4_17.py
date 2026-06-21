def categorize_value(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")
    if n < 0:
        return 'low'
    if n < 50:
        return 'medium'
    return 'high'

if __name__ == '__main__':
    print(categorize_value(10))
    print(categorize_value(50))
    print(categorize_value(100))
    print(categorize_value(-5))
    print(categorize_value(49))