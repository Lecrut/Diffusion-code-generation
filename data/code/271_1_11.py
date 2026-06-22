def filter_alphabetic_strings(strings):
    alphabetic_strings = []
    for string in strings:
        if all(char.isalpha() for char in string):
            alphabetic_strings.append(string)
    return alphabetic_strings

if __name__ == '__main__':
    sample_values = ["apple", "banana", "1234", "cherry", "!@#"]
    filtered_list = filter_alphabetic_strings(sample_values)
    print(filtered_list)