def find_smallest_lexicographical(strings):
    if not strings:
        return None
    smallest = min(strings)
    return smallest
if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry', 'date']
    result = find_smallest_lexicographical(sample_strings)
    print(result)