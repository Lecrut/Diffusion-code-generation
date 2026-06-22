def filter_strings(strings):
    return [s for s in strings if len(s) <= 5]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date", "elderberry"]
    result = filter_strings(sample_values)
    print(result)