def compare_adjacent_strings(strings):
    results = []
    for i in range(len(strings) - 1):
        if strings[i] < strings[i + 1]:
            results.append("Ascending")
        elif strings[i] > strings[i + 1]:
            results.append("Descending")
        else:
            results.append("Equal")
    return results

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(compare_adjacent_strings(sample_strings))