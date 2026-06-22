def find_difference(num1, num2):
    return abs(num1 - num2)

if __name__ == '__main__':
    sample_values = {
        'example1': {'a': 10, 'b': 4},
        'example2': {'a': -5, 'b': 15},
        'example3': {'a': 7.5, 'b': 3.2},
        'example4': {'a': 0, 'b': 0}
    }
    
    for key, values in sample_values.items():
        result = find_difference(values['a'], values['b'])
        print(f"The absolute difference between {values['a']} and {values['b']} is: {result}")