def categorize_number(num):
    return 'low' if num < 30 else 'medium' if num < 60 else 'high'
if __name__ == '__main__':
    print(categorize_number(25))
    print(categorize_number(45))
    print(categorize_number(75))