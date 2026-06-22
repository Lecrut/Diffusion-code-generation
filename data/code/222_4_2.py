def find_min_lexicographical(strings):
    if not strings:
        return None
    min_str = strings[0]
    for string in strings[1:]:
        if string < min_str:
            min_str = string
    return min_str

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    print(find_min_lexicographical(sample_values))