def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    sample_values = {('a1', 'b1'): (100, 45), ('a2', 'b2'): (50, 150)}
    
    for label, (a, b) in sample_values.items():
        result = subtract_numbers(a, b)
        print(f"Result of {label}: {result}")