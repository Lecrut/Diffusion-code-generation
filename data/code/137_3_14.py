def categorize_number(num: int) -> str:
    if num < 50:
        return 'small'
    elif num < 100:
        return 'medium'
    else:
        return 'large'
if __name__ == '__main__':
    print(categorize_number(45))
    print(categorize_number(75))
    print(categorize_number(120))