def categorize_number(value):
    if value < 0:
        return 'low'
    elif value < 100:
        return 'medium'
    else:
        return 'high'

if __name__ == '__main__':
    print(categorize_number(-5))
    print(categorize_number(50))
    print(categorize_number(150))