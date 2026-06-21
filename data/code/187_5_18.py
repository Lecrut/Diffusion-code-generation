def find_largest_string_by_length(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All items in the list must be strings")
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    largest_string = find_largest_string_by_length(sample_strings)
    print(largest_string)