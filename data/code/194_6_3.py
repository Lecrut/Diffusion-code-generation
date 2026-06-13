def find_longest_string(iterable):
    if not iterable:
        return None
    longest_string = ""
    for s in iterable:
        if len(s) > len(longest_string):
            longest_string = s
    yield longest_string
if __name__ == '__main__':
    sample_data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result_generator = find_longest_string(sample_data)
    longest = None
    for item in result_generator:
        longest = item
    print(longest)