def filter_alphabetic_strings(strings):
    return [s for s in strings if s.isalpha()]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "123", "!@#"]
    filtered_list = filter_alphabetic_strings(sample_values)
    print(filtered_list)