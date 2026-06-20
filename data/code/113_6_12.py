def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    sample_values = {
        'a1': 100,
        'b1': 45,
        'a2': 50,
        'b2': 150
    }
    
    for key, value in sample_values.items():
        if key.endswith('1'):
            a, b = value, sample_values[key.replace('1', '2')]
            result = subtract_numbers(a, b)
            print(f"Result of {a} - {b}: {result}")