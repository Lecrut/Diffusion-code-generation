def find_longest_list_item(string_list):
    if not isinstance(string_list, list) or not all(isinstance(item, str) for item in string_list):
        raise ValueError("Input must be a list of strings")
    
    longest_string = ""
    for s in string_list:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_list_item(sample_list)
    print(result)