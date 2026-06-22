def find_min_lexicographical(strings):
    if not strings:
        return None
    min_string = strings[0]
    for string in strings:
        if string < min_string:
            min_string = string
    return min_string

if __name__ == '__main__':
    sample_strings = ["banana", "apple", "cherry"]
    print(find_min_lexicographical(sample_strings))