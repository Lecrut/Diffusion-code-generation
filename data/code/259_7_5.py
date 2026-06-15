import sys
def find_min_max_strings(string_list):
    if not string_list:
        return None, None
    minimum = string_list[0]
    maximum = string_list[0]
    for s in string_list[1:]:
        if s < minimum:
            minimum = s
        if s > maximum:
            maximum = s
    return minimum, maximum
if __name__ == '__main__':
    sample_list = ["apple", "zebra", "banana", "cat", "antelope"]
    min_val, max_val = find_min_max_strings(sample_list)
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")