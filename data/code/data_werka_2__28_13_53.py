def is_larger_than(first_number, second_number):
    return first_number > second_number

if __name__ == '__main__':
    comparison_values = {
        'first_value': 25,
        'second_value': 15
    }
    
    result = is_larger_than(comparison_values['first_value'], comparison_values['second_value'])
    print(result)