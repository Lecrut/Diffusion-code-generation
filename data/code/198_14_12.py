def find_smallest_string(strings):
    if not strings:
        raise ValueError("Input list is empty.")
    
    return min(strings)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    try:
        smallest_string = find_smallest_string(sample_strings)
        print(smallest_string)
    except ValueError as e:
        print(e)