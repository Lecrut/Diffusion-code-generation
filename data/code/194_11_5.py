def find_longest_string(string_list):
    if not string_list:
        raise ValueError("Input list cannot be empty")
    
    longest_string = max(string_list, key=len)
    return longest_string

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    try:
        result = find_longest_string(sample_list)
        print(result)
    except ValueError as e:
        print(e)