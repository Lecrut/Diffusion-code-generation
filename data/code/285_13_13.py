def compare_adjacent_strings(strings):
    return [max(strings[i:i+2]) for i in range(len(strings) - 1)]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    result = compare_adjacent_strings(sample_values)
    print(result)