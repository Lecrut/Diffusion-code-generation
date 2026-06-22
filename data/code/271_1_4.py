def filter_alphabetic_strings(strings):
    alphabetic_strings = []
    for s in strings:
        if s.isalpha():
            alphabetic_strings.append(s)
    return alphabetic_strings

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry123", "date!", "elderberry"]
    filtered_list = filter_alphabetic_strings(sample_values)
    print(filtered_list)