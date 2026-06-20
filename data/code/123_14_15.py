def sum_dictionary_values():
    sample_dict = {
        'a': 10,
        'b': 25,
        'c': 'hello',
        'd': 30,
        'e': -5
    }
    
    total = sum(value for value in sample_dict.values() if isinstance(value, (int, float)))
    return total

if __name__ == '__main__':
    result = sum_dictionary_values()
    print(result)