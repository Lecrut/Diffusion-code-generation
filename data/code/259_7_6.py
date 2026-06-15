def find_min_max_strings(string_list):
    if not string_list:
        return None, None
    min_string = string_list[0]
    max_string = string_list[0]
    for s in string_list[1:]:
        if s < min_string:
            min_string = s
        if s > max_string:
            max_string = s
    return min_string, max_string
if __name__ == '__main__':
    sample_list = ["apple", "zebra", "banana", "cat", "ant"]
    minimum, maximum = find_min_max_strings(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum lexicographical string: {minimum}")
    print(f"Maximum lexicographical string: {maximum}")