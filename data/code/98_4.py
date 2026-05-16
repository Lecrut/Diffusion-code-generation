def categorize_number(n):
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
    print(categorize_number(9))
    print(categorize_number(50))
    print(categorize_number(101))