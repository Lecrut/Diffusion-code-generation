def categorize_number(num: int) -> str:
    if num < 10:
        return 'small'
    elif num < 100:
        return 'medium'
    else:
        return 'large'

if __name__ == '__main__':
    sample_values = [5, 45, 120]
    for value in sample_values:
        print(f'{value}: {categorize_number(value)}')