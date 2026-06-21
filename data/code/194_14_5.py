def find_longest_string(strings):
    max_length = 0
    longest_string = ""
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))