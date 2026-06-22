def compare_adjacent_strings(strings):
    return [max(pair) for pair in zip(strings[:-1], strings[1:])]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    result = compare_adjacent_strings(sample_values)
    print(result)