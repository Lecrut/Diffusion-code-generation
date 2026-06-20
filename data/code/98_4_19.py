def categorize_number(n):
    ranges = {
        'low': (10, 50),
        'medium': (50, 100),
        'high': (100, float('inf'))
    }
    for category, (min_val, max_val) in ranges.items():
        if min_val <= n < max_val:
            return category

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(35))
    print(categorize_number(100))
    print(categorize_number(9))
    print(categorize_number(50))
    print(categorize_number(101))