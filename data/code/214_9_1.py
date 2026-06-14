def find_smallest_string(list_of_strings):
    if not list_of_strings:
        return None
    smallest = list_of_strings[0]
    for s in list_of_strings[1:]:
        if s < smallest:
            smallest = s
    return smallest
if __name__ == '__main__':
    sample_list = ["banana", "apple", "zebra", "cat", "apricot"]
    result = find_smallest_string(sample_list)
    print(result)