def find_longest_string(string_list):
    if not string_list:
        raise ValueError("Input list cannot be empty")
    
    longest_string = max(string_list, key=len)
    return longest_string

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    try:
        result = find_longest_string(sample_strings)
        print(result)
    except ValueError as e:
        print(e)