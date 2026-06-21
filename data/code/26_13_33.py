def compare_integers(a, b):
    return a > b

if __name__ == '__main__':
    test_values = {
        'test1': (10, 5),
        'test2': (3, 8),
        'test3': (7, 7)
    }
    
    for name, values in test_values.items():
        result = compare_integers(*values)
        print(f"{name}: {result}")