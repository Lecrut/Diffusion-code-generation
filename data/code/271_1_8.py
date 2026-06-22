def filter_alphabetic(strings):
    return [s for s in strings if s.isalpha()]

if __name__ == '__main__':
    sample_values = ["hello", "world", "123", "test"]
    result = filter_alphabetic(sample_values)
    print(result)