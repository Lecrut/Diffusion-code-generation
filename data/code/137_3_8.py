def categorize_number(num: int) -> str:
    if num < 50:
        return 'small'
    elif num < 200:
        return 'medium'
    else:
        return 'large'
if __name__ == '__main__':
    print(categorize_number(49))
    print(categorize_number(100))
    print(categorize_number(250))