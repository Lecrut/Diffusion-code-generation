def find_smallest_string(strings):
    if not strings:
        return None
    smallest = min(strings)
    return smallest
if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry']
    result = find_smallest_string(sample_strings)
    print(result)