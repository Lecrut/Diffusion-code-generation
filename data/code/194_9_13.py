def longest_string(strings):
    if not hasattr(strings, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    return max((s for s in strings if isinstance(s, str)), key=len, default=None)

if __name__ == '__main__':
    sample = ["apple", "banana", "cherry"]
    print(longest_string(sample))