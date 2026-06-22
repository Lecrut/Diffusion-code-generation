def compare_two_simple_quantities_now_convert_all(quantity1, quantity2):
    return quantity1 + quantity2

if __name__ == '__main__':
    sample_values = {
        'a': 5,
        'b': 3,
        'c': 7,
        'd': 4,
        'e': 10
    }
    
    for key in ['a', 'c', 'e']:
        result = compare_two_simple_quantities_now_convert_all(sample_values[key], sample_values[key + 1])
        print(result)