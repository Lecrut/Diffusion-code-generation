def find_longest_list_item(string_list):
    if not string_list:
        raise ValueError("Input list cannot be empty")
    longest_string = string_list[0]
    for item in string_list:
        if len(item) > len(longest_string):
            longest_string = item
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    try:
        result = find_longest_list_item(sample_list)
        print(result)
    except ValueError as e:
        print(e)