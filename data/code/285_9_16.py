def compare_adjacent_strings(strings):
    results = []
    for i in range(len(strings) - 1):
        if strings[i] < strings[i + 1]:
            results.append('ascending')
        elif strings[i] > strings[i + 1]:
            results.append('descending')
        else:
            results.append('equal')
    return results

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(compare_adjacent_strings(sample_strings))