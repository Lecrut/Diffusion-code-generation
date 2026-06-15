def find_longest_string(list_of_lists):
    longest_string = ""
    max_length = -1
    for inner_list in list_of_lists:
        for item in inner_list:
            if len(item) > max_length:
                max_length = len(item)
                longest_string = item
    return longest_string
if __name__ == '__main__':
    sample_data = [
        ["apple", "banana", "kiwi"],
        ["grapefruit", "melon", "orange"],
        ["strawberry", "fig"]
    ]
    result = find_longest_string(sample_data)
    print(result)