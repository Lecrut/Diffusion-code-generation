def categorize_number(number: int) -> str:
    if number < 30:
        return 'small'
    elif number < 60:
        return 'medium'
    else:
        return 'large'

if __name__ == '__main__':
    sample_values = [25, 45, 75]
    for value in sample_values:
        print(f'{value}: {categorize_number(value)}')