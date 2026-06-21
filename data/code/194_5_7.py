def longest_string(iterable):
    max_length = 0
    longest_str = None
    for item in iterable:
        if isinstance(item, str) and len(item) > max_length:
            max_length = len(item)
            longest_str = item
    return longest_str

if __name__ == '__main__':
    sample_iterable = ["short", "longer string", "even longer string here"]
    print(longest_string(sample_iterable))