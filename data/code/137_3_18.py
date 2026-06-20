def categorize_number(num: int) -> str:
    if num < 50:
        return 'small'
    elif num < 200:
        return 'medium'
    else:
        return 'large'

if __name__ == '__main__':
    sample_values = [45, 100, 250]
    for value in sample_values:
        print(f'{value}: {categorize_number(value)}')