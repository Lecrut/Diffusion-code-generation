def find_longest_string(strings):
    max_length = 0
    longest_string = ""
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
    return longest_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_longest_string(sample_strings))