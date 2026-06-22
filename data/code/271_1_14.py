def filter_alphabetic_strings(strings):
    return [s for s in strings if all(c.isalpha() for c in s)]

if __name__ == '__main__':
    sample_values = ["hello", "world", "123", "test", "!@#"]
    result = filter_alphabetic_strings(sample_values)
    print(result)