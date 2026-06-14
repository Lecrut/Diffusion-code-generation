def find_min_max_strings(string_list):
    if not string_list:
        return None, None
    minimum = string_list[0]
    maximum = string_list[0]
    for s in string_list:
        if s < minimum:
            minimum = s
        if s > maximum:
            maximum = s
    return minimum, maximum
if __name__ == '__main__':
    sample_list = ["apple", "zebra", "banana", "cat", "ant"]
    min_val, max_val = find_min_max_strings(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum lexicographical value: {min_val}")
    print(f"Maximum lexicographical value: {max_val}")
    sample_list_2 = ["zoo", "ant", "bear", "lion"]
    min_val_2, max_val_2 = find_min_max_strings(sample_list_2)
    print(f"\nList: {sample_list_2}")
    print(f"Minimum lexicographical value: {min_val_2}")
    print(f"Maximum lexicographical value: {max_val_2}")
    empty_list = []
    min_val_3, max_val_3 = find_min_max_strings(empty_list)
    print(f"\nList: {empty_list}")
    print(f"Minimum lexicographical value: {min_val_3}")
    print(f"Maximum lexicographical value: {max_val_3}")