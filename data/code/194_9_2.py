def find_longest_string(input_list):
    if not hasattr(input_list, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    longest = ""
    for item in input_list:
        if isinstance(item, str) and len(item) > len(longest):
            longest = item
    
    return longest

if __name__ == '__main__':
    sample_input = ["apple", "banana", "cherry", 123, None]
    try:
        result = find_longest_string(sample_input)
        print(result)
    except ValueError as e:
        print(e)