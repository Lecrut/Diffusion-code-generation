def filter_strings(strings):
    return [s for s in strings if s.isalpha()]

if __name__ == '__main__':
    sample_values = ["hello", "world!", "Python3", "filter", "123"]
    filtered_values = filter_strings(sample_values)
    print(filtered_values)