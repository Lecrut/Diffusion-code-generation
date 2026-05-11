def count_string_occurrences(list_of_strings):
    counts = {}
    for item in list_of_strings:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
if __name__ == '__main__':
    sample_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_string_occurrences(sample_list)
    print(result)