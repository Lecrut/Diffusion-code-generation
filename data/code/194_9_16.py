def longest_string(strings):
    if not hasattr(strings, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    return max((s for s in strings if isinstance(s, str)), key=len, default=None)

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", 123]
    try:
        result = longest_string(sample_values)
        print(result)
    except ValueError as e:
        print(e)