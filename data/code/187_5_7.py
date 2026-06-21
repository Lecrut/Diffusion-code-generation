MAX_STRING_LENGTH_KEY = 'length'

def find_largest_string_by_length(strings):
    return max(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    largest_string = find_largest_string_by_length(sample_strings)
    print(largest_string)