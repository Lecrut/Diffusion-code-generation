def filter_alphabetic_strings(strings):
    return [s for s in strings if s.isalpha()]

if __name__ == '__main__':
    sample_values = ["hello", "world", "123", "test", "sample"]
    result = filter_alphabetic_strings(sample_values)
    print(result)