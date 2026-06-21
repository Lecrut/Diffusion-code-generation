def longest_string(lst):
    if not hasattr(lst, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    return max(lst, key=len) if lst else None

if __name__ == '__main__':
    sample = ["short", "longer string", "longest"]
    print(longest_string(sample))