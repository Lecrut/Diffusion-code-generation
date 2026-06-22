def compare_adjacent_strings(strings):
    results = []
    for i in range(len(strings) - 1):
        str1 = strings[i]
        str2 = strings[i + 1]
        if str1 < str2:
            result = "Ascending"
        elif str1 > str2:
            result = "Descending"
        else:
            result = "Equal"
        results.append((str1, str2, result))
    return results

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(compare_adjacent_strings(sample_strings))