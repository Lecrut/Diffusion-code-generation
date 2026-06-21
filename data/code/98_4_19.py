def validate_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if n != n:
        raise ValueError("Input cannot be NaN")
    return n

def categorize_number(n):
    validate_number(n)
    if n < 10:
        return 'low'
    if n < 50:
        return 'medium'
    return 'high'

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(35))
    print(categorize_number(100))
    print(categorize_number(-5))
    print(categorize_number(49))
    print(categorize_number(50))