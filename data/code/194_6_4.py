def find_longest_string(iterable):
    if not iterable:
        return None
    longest_string = ""
    max_length = -1
    for s in iterable:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
    yield longest_string
if __name__ == '__main__':
    sample_data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result_generator = find_longest_string(sample_data)
    longest = None
    for item in result_generator:
        longest = item
    print(longest)