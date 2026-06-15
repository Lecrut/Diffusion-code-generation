def find_min_max_strings(string_list):
    if not string_list:
        return None, None
    min_str = string_list[0]
    max_str = string_list[0]
    for s in string_list[1:]:
        if s < min_str:
            min_str = s
        if s > max_str:
            max_str = s
    return min_str, max_str
if __name__ == '__main__':
    sample_list = ["apple", "zebra", "banana", "cat", "antelope"]
    minimum, maximum = find_min_max_strings(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum lexicographical string: {minimum}")
    print(f"Maximum lexicographical string: {maximum}")