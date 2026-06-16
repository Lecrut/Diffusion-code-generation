def find_largest_string(list_of_strings):
    if not list_of_strings:
        return None
    largest = list_of_strings[0]
    for s in list_of_strings[1:]:
        if s > largest:
            largest = s
    return largest
if __name__ == '__main__':
    sample_list = ["apple", "zebra", "banana", "cat"]
    result = find_largest_string(sample_list)
    print(result)