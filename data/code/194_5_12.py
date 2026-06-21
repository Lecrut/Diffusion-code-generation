def longest_string_generator(iterable):
    max_length = 0
    longest_str = None
    for item in iterable:
        if isinstance(item, str) and len(item) > max_length:
            max_length = len(item)
            longest_str = item
        yield longest_str

if __name__ == '__main__':
    sample_iterable = ["short", "longer string", "even longer string here", "tiny"]
    longest_gen = longest_string_generator(sample_iterable)
    for _ in range(len(sample_iterable)):
        print(next(longest_gen))