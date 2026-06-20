def sum_three_numbers(a, b, c):
    return a + b + c

if __name__ == '__main__':
    sample_values = {
        'integers': (10, 5, 2),
        'mixed_types': ('hello', 5, 2),
        'floats': (3.14, 2, 1.5)
    }
    
    for key, values in sample_values.items():
        result = sum_three_numbers(*values)
        print(f"Sum of {key}: {result}")