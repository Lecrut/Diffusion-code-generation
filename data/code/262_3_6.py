def find_extremes_by_length(strings):
    if not strings:
        return None, None
    min_str = max_str = strings[0]
    for s in strings[1:]:
        if len(s) < len(min_str):
            min_str = s
        elif len(s) > len(max_str):
            max_str = s
    return min_str, max_str

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_extremes_by_length(sample_strings))