def compare_adjacent_strings(strings):
    result = []
    for i in range(len(strings) - 1):
        if strings[i] != strings[i+1]:
            result.append(max(strings[i], strings[i+1]))
    return result

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    processed_values = compare_adjacent_strings(sample_values)
    for value in processed_values:
        print(value)