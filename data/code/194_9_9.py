def longest_string(lst):
    if not hasattr(lst, '__iter__'):
        raise ValueError("Input is not iterable")
    
    longest = None
    max_length = 0
    
    for item in lst:
        if isinstance(item, str) and len(item) > max_length:
            longest = item
            max_length = len(item)
    
    return longest

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    print(longest_string(sample_list))