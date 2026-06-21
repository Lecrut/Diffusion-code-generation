def case_insensitive_sort(strings):
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sample_strings = ['Lemon', 'lime', 'Kiwi', 'mango', 'Apple']
    sorted_result = case_insensitive_sort(sample_strings)
    print("Sorted Strings:")
    for string in sorted_result:
        print(string)