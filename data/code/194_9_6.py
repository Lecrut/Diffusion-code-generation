def longest_string(lst):
    if not hasattr(lst, '__iter__'):
        raise ValueError("Input is not iterable")
    return max((s for s in lst if isinstance(s, str)), key=len, default=None)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", 123, None]
    result = longest_string(sample_list)
    print(result)