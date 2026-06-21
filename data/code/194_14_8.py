def find_longest_string(list_of_lists):
    max_length = -1
    longest_string = ""
    for sublist in list_of_lists:
        for item in sublist:
            if len(item) > max_length:
                max_length = len(item)
                longest_string = item
    return longest_string

if __name__ == '__main__':
    sample_data = [
        ["apple", "banana", "kiwi"],
        ["grapefruit", "orange", "melon"],
        ["strawberry", "pineapple", "avocado"]
    ]
    result = find_longest_string(sample_data)
    print(result)