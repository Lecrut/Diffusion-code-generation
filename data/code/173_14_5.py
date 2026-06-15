def group_strings_by_length(string_list):
    grouped = {}
    for s in string_list:
        length = len(s)
        if length not in grouped:
            grouped[length] = []
        grouped[length].append(s)
    return grouped
if __name__ == '__main__':
    sample_strings = ["apple", "bat", "cat", "dog", "elephant", "ant", "fig"]
    result = group_strings_by_length(sample_strings)
    print(result)