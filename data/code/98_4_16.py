def categorize_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if n < 10:
        return 'low'
    elif n < 50:
        return 'medium'
    else:
        return 'high'

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(35))
    print(categorize_number(100))
    try:
        print(categorize_number('a'))
    except ValueError as e:
        print(e)