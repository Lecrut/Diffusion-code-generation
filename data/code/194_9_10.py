def longest_string(lst):
    if not hasattr(lst, '__iter__'):
        raise ValueError("Input is not iterable")
    
    return max((s for s in lst if isinstance(s, str)), key=len, default=None)

if __name__ == '__main__':
    sample = ["apple", "banana", "cherry", 123]
    try:
        print(longest_string(sample))
    except ValueError as e:
        print(e)