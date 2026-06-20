def calculate_three_sum(a: float, b: float, c: float) -> float:
    return a + b + c

if __name__ == '__main__':
    sample_values = {
        'sample1': (1.0, 2.0, 3.0),
        'sample2': (1.5, 2.5, 3.0)
    }
    
    for key, values in sample_values.items():
        result = calculate_three_sum(*values)
        print(f"{key}: {result}")