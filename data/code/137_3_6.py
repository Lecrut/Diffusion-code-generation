def categorize_number(number: int) -> str:
    if number < 10:
        return 'small'
    elif number < 100:
        return 'medium'
    else:
        return 'large'

if __name__ == '__main__':
    sample_values = [5, 45, 123]
    for value in sample_values:
        print(f'{value}: {categorize_number(value)}')