def find_max_length_string(strings):
    max_str = ""
    for s in strings:
        if len(s) > len(max_str):
            max_str = s
    return max_str

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_max_length_string(sample_strings))