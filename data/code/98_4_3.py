def categorize_number(n):
    if n < 100:
        return 'low'
    elif n < 500:
        return 'medium'
    else:
        return 'high'
if __name__ == '__main__':
    print(categorize_number(50))
    print(categorize_number(350))
    print(categorize_number(1200))