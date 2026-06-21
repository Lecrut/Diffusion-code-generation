def find_longest_string(string_list):
    if not string_list:
        return None
    longest = ""
    for s in string_list:
        if len(s) > len(longest):
            longest = s
    return longest

if __name__ == '__main__':
    sample_list = ["apple", "banana", "orange", "kiwi", "grapefruit"]
    result = find_longest_string(sample_list)
    print(result)

    empty_list = []
    result_empty = find_longest_string(empty_list)
    print(result_empty)

    single_item_list = ["longest"]
    result_single = find_longest_string(single_item_list)
    print(result_single)