def find_lexicographical_maximum(list_of_strings):
    if not list_of_strings:
        return None
    max_string = list_of_strings[0]
    for s in list_of_strings:
        if s > max_string:
            max_string = s
    return max_string
if __name__ == '__main__':
    sample_list = ["apple", "zebra", "banana", "cat"]
    result = find_lexicographical_maximum(sample_list)
    print(result)
    sample_list_2 = ["zoo", "ant", "bear", "lion"]
    result_2 = find_lexicographical_maximum(sample_list_2)
    print(result_2)
    sample_list_3 = ["a", "b", "c", "aa"]
    result_3 = find_lexicographical_maximum(sample_list_3)
    print(result_3)
    sample_list_4 = []
    result_4 = find_lexicographical_maximum(sample_list_4)
    print(result_4)