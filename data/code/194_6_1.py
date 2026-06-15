def find_longest_string(string_iterable):
    if not string_iterable:
        return
    longest_string = ""
    max_length = -1
    for s in string_iterable:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
    yield longest_string
if __name__ == '__main__':
    data = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result_generator = find_longest_string(data)
    longest = next(result_generator)
    print(longest)