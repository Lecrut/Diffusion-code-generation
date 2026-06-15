def find_max_string(list_of_strings):
    if not list_of_strings:
        return None
    max_string = list_of_strings[0]
    for s in list_of_strings:
        if s > max_string:
            max_string = s
    return max_string
if __name__ == '__main__':
    sample_list = ["apple", "zebra", "banana", "cat"]
    maximum = find_max_string(sample_list)
    print(maximum)
    sample_list_2 = ["zoo", "ant", "bear", "lion"]
    maximum_2 = find_max_string(sample_list_2)
    print(maximum_2)
    sample_list_3 = ["a", "b", "c", "aa", "ab"]
    maximum_3 = find_max_string(sample_list_3)
    print(maximum_3)