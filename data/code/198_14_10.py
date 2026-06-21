def find_smallest_lexicographical(strings):
    if not strings:
        raise ValueError("Input list is empty.")
    
    smallest = min(strings)
    return smallest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    try:
        result = find_smallest_lexicographical(sample_strings)
        print(result)
    except ValueError as e:
        print(e)