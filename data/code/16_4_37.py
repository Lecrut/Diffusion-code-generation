def positive_filter(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    for item in iterable:
        if not isinstance(item, (int, float)):
            raise ValueError("All items in the iterable must be numbers")
        
        if item > 0:
            yield True

if __name__ == '__main__':
    sample_values = [-15.5, -3, 0, 2, 6.7, -1, 4.2]
    result = list(positive_filter(sample_values))
    print(result)