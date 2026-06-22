def compare_adjacent_strings(str_list):
    results = []
    for i in range(len(str_list) - 1):
        str1, str2 = str_list[i], str_list[i + 1]
        if str1 < str2:
            results.append((str1, str2, 'Ascending'))
        elif str1 > str2:
            results.append((str1, str2, 'Descending'))
        else:
            results.append((str1, str2, 'Equal'))
    return results

if __name__ == '__main__':
    sample_strings = [
        "apple",
        "banana",
        "cherry",
        "date"
    ]
    comparison_results = compare_adjacent_strings(sample_strings)
    print(comparison_results)