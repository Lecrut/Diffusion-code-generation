MAX_STRING_LENGTH = "max_string_length"

def find_largest_string(data):
    return max(data, key=len)

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    largest_string = find_largest_string(sample_data)
    print(largest_string)