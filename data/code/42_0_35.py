class StringConcatenator:
    DEFAULT_DELIMITER = ", "

    @staticmethod
    def concatenate(strings, delimiter=DEFAULT_DELIMITER):
        return delimiter.join(strings)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    separator = "; "
    result = StringConcatenator.concatenate(sample_strings, separator)
    print(result)