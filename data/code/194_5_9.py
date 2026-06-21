def longest_string(iterable):
    longest = None
    for item in iterable:
        if isinstance(item, str) and (longest is None or len(item) > len(longest)):
            longest = item
    return longest

if __name__ == '__main__':
    sample_values = ['apple', 'banana', 'cherry', 'date']
    print(longest_string(sample_values))