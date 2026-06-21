def calculate_list_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_values = {
        'integers': [1, 2, 3, 4, 5],
        'decimals': [10.5, 20.5, 30.0],
        'mixed': [-1, 5, -3, 10]
    }
    
    for category, values in sample_values.items():
        result = calculate_list_sum(values)
        print(f'Sum of {category}: {result}')