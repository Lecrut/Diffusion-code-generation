def compare_adjacent_strings(string_list):
    return [max(pair) for pair in zip(string_list, string_list[1:])]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    result = compare_adjacent_strings(sample_values)
    print(result)