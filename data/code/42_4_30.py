class StringConcatenator:
    DEFAULT_SEPARATOR = " "

    @staticmethod
    def concatenate_segments(iterable, separator=DEFAULT_SEPARATOR):
        for segment in iterable:
            yield segment
            yield separator

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python"]
    custom_separator = "-"
    generator = StringConcatenator.concatenate_segments(sample_strings, custom_separator)
    result = "".join(generator).rstrip(custom_separator)
    print(result)