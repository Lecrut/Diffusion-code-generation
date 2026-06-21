def longest_string_generator(iterable):
    longest = None
    for item in iterable:
        if isinstance(item, str) and (longest is None or len(item) > len(longest)):
            longest = item
            yield longest

if __name__ == '__main__':
    sample_iterable = ["short", "longer string here", "another example"]
    longest_str_gen = longest_string_generator(sample_iterable)
    for result in longest_str_gen:
        print(result)