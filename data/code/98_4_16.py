CATEGORIES = {
    'low': (0, 10),
    'medium': (10, 50),
    'high': (50, 100)
}

def categorize_number(n):
    for label, (start, end) in CATEGORIES.items():
        if start <= n < end:
            return label
    return 'unknown'

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(25))
    print(categorize_number(75))
    print(categorize_number(15))
    print(categorize_number(50))
    print(categorize_number(0))