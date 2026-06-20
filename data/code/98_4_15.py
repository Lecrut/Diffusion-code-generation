def categorize_number(n):
    ranges = {
        'low': (0, 10),
        'medium': (10, 50),
        'high': (50, float('inf'))
    }
    
    for category, (lower, upper) in ranges.items():
        if lower <= n < upper:
            return category

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(35))
    print(categorize_number(100))
    print(categorize_number(9))
    print(categorize_number(50))
    print(categorize_number(51))