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
    data = ["apple", "zebra", "banana", "cat", "apricot"]
    minimum, maximum = find_min_max_strings(data)
    print(f"Minimum string: {minimum}")
    print(f"Maximum string: {maximum}")