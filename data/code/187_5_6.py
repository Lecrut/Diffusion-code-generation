def find_largest_string_by_length(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_largest_string_by_length(sample_strings))