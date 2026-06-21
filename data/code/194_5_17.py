def longest_string(iterable):
    max_len = 0
    longest = None
    for item in iterable:
        if len(item) > max_len:
            max_len = len(item)
            longest = item
    return longest

if __name__ == '__main__':
    sample_iterable = ["apple", "banana", "cherry", "date"]
    print(longest_string(sample_iterable))