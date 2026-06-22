def compare_adjacent_strings(strings):
    result = []
    for i in range(len(strings) - 1):
        if strings[i] != strings[i+1]:
            later_string = max(strings[i], strings[i+1])
            result.append(later_string)
    return result

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    result = compare_adjacent_strings(sample_values)
    print(result)