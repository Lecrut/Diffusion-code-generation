def add_numbers(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Both inputs must be numbers."

if __name__ == '__main__':
    sample_values = {
        'case1': (5, 10),
        'case2': ('a', 10),
        'case3': (3.5, 4.5),
        'case4': (0, 0)
    }
    
    for key, values in sample_values.items():
        result = add_numbers(*values)
        print(f"{key}: {result}")