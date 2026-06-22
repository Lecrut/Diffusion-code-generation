def filter_strings(strings):
    return [s for s in strings if len(s) <= 5]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date", "elderberry"]
    filtered_list = filter_strings(sample_strings)
    print(filtered_list)