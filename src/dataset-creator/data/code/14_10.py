def count_string_occurrences(string_list):
    counts = {}
    for item in string_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
if __name__ == '__main__':
    sample_strings = [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple",
        "grape"
    ]
    result_dict = count_string_occurrences(sample_strings)
    print(result_dict)