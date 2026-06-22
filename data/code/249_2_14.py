def find_max_lexicographically(strings):
    if not strings:
        return None
    max_string = strings[0]
    for string in strings[1:]:
        if string > max_string:
            max_string = string
    return max_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_max_lexicographically(sample_strings))