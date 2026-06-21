def longest_string(lst):
    if not hasattr(lst, '__iter__'):
        raise ValueError("Input is not iterable")
    
    return max((s for s in lst if isinstance(s, str)), key=len, default=None)

if __name__ == '__main__':
    sample = ["short", "longer string", "longest_string_is_here"]
    print(longest_string(sample))