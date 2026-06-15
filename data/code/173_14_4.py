def group_strings_by_length(string_list):
    grouped_dict = {}
    for s in string_list:
        length = len(s)
        if length not in grouped_dict:
            grouped_dict[length] = []
        grouped_dict[length].append(s)
    return grouped_dict
if __name__ == '__main__':
    sample_strings = ["apple", "bat", "cat", "dog", "elephant", "ant", "ball"]
    result = group_strings_by_length(sample_strings)
    print(result)