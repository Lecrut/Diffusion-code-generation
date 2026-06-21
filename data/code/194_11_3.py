def find_max_length_string(strings):
    max_length = 0
    max_string = ""
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            max_string = string
    return max_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_max_length_string(sample_strings))