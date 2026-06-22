def find_min_lexicographical(strings):
    if not strings:
        raise ValueError("List is empty")
    min_string = min(strings)
    return min_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    print(find_min_lexicographical(sample_strings))