def categorize_number(n):
    return 'low' if n < 10 else ('medium' if n < 50 else 'high')

if __name__ == '__main__':
    print(categorize_number(5))
    print(categorize_number(35))
    print(categorize_number(100))
    print(categorize_number(9))
    print(categorize_number(50))
    print(categorize_number(101))