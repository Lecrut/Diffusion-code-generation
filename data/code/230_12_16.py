def filter_long_strings(strings):
    return [s for s in strings if len(s) <= 5]

if __name__ == '__main__':
    sample_data = ["apple", "banana", "kiwi", "cherry", "date"]
    result = filter_long_strings(sample_data)
    print(result)