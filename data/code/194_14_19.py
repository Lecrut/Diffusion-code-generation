def find_longest_string(list_of_strings):
    max_length = 0
    longest_string = ""
    for item in list_of_strings:
        if len(item) > max_length:
            max_length = len(item)
            longest_string = item
    return longest_string

if __name__ == '__main__':
    sample_data = [
        "apple", 
        "banana", 
        "cherry", 
        "date", 
        "elderberry"
    ]
    result = find_longest_string(sample_data)
    print(result)