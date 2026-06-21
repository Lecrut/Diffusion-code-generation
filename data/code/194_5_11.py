def longest_string_generator(iterable):
    max_length = 0
    longest_str = ""
    for item in iterable:
        if isinstance(item, str) and len(item) > max_length:
            max_length = len(item)
            longest_str = item
            yield longest_str

if __name__ == '__main__':
    sample_data = ["apple", "banana", "programming", "algorithm", "supercalifragilisticexpialidocious"]
    generator = longest_string_generator(sample_data)
    print(next(generator))