def sum_numbers(numbers):
    return sum(numbers)

if __name__ == '__main__':
    samples = {
        'positive': [1, 2, 3],
        'empty': []
    }
    
    for label, sample in samples.items():
        result = sum_numbers(sample)
        print(f'Sum of {label} list: {result}')