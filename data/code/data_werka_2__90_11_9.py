def check_leading_a_or_b(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    valid_prefixes = ('A', 'B')
    
    for item in input_list:
        if not isinstance(item, str):
            raise TypeError("All items must be strings")
        if item and item[0] in valid_prefixes:
            return True
    return False

if __name__ == '__main__':
    data = ['Avocado', 'Banana', 'Cherry']
    result = check_leading_a_or_b(data)
    print(result)