def longest_string(lst):
    if not hasattr(lst, '__iter__') or isinstance(lst, str):
        raise ValueError('Input must be an iterable other than a string')
    return max(lst, key=len) if lst else None
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    print(longest_string(sample_list))