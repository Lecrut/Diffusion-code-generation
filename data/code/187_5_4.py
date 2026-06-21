def find_largest_string_by_length(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["strawberry", "apple", "banana", "cherry"]
    largest_string = find_largest_string_by_length(sample_strings)
    print(largest_string)