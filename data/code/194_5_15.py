def longest_string_generator(iterable):
    longest = None
    for item in iterable:
        if longest is None or len(item) > len(longest):
            longest = item
        yield longest

if __name__ == '__main__':
    sample_iterable = ["apple", "banana", "cherry", "date"]
    longest_gen = longest_string_generator(sample_iterable)
    for _ in range(len(sample_iterable)):
        print(next(longest_gen))