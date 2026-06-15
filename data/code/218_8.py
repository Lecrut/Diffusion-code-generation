def find_lexicographically_smallest(string_list):
    if not string_list:
        return None
    smallest = string_list[0]
    for s in string_list[1:]:
        if s < smallest:
            smallest = s
    return smallest
if __name__ == '__main__':
    sample_strings = ["apple", "zebra", "banana", "cat", "apricot"]
    result = find_lexicographically_smallest(sample_strings)
    print(result)