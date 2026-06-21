def get_longest_string(string_list):
    if not isinstance(string_list, list) or not all(isinstance(item, str) for item in string_list):
        raise ValueError("Input must be a list of strings")
    
    longest_string = ""
    max_length = 0
    
    for s in string_list:
        length = len(s)
        if length > max_length:
            max_length = length
            longest_string = s
    
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = get_longest_string(sample_list)
    print(result)