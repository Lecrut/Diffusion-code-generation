def find_longest_string(list_of_strings):
    longest_string = ""
    max_length = 0
    for string in list_of_strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string

if __name__ == '__main__':
    sample_data = [
        "apple", "banana", "kiwi",
        "grapefruit", "orange", "melon",
        "strawberry", "pineapple", "avocado"
    ]
    result = find_longest_string(sample_data)
    print(result)