def sum_numbers(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_values = {
        'non_empty': [10, 20, 30],
        'empty': []
    }
    
    for key, value in sample_values.items():
        print(f"Sum of {key} list: {sum_numbers(value)}")