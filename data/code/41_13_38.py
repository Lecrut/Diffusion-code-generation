def process_string(input_string):
    operations = {
        'lower': str.lower,
        'swapcase': str.swapcase
    }
    
    result = input_string
    for operation in operations.values():
        result = operation(result)
    
    return result

if __name__ == '__main__':
    test_value = 'Hello World'
    result = process_string(test_value)
    print(result)