def reverse_string_list(input_list):
    return input_list[::-1]

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    reversed_strings = reverse_string_list(sample_strings)
    for string in reversed_strings:
        print(string)