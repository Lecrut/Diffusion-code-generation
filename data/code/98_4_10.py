def categorize_number(n):
    LOW_THRESHOLD = 10
    MEDIUM_THRESHOLD = 50
    
    if n < LOW_THRESHOLD:
        return 'low'
    elif n < MEDIUM_THRESHOLD:
        return 'medium'
    else:
        return 'high'

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(35))
    print(categorize_number(100))
    print(categorize_number(9))
    print(categorize_number(50))
    print(categorize_number(51))