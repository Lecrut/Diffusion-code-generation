class StringSeparator:
    def __init__(self):
        self._separated_chars = []
    def split_string(self, input_string):
        self._separated_chars = list(input_string)
    def get_separated_chars(self):
        return self._separated_chars
if __name__ == '__main__':
    separator = StringSeparator()
    sample_string_1 = "hello"
    separator.split_string(sample_string_1)
    result_1 = separator.get_separated_chars()
    print(f"Input: {sample_string_1}")
    print(f"Output: {result_1}")
    sample_string_2 = "world"
    separator.split_string(sample_string_2)
    result_2 = separator.get_separated_chars()
    print(f"Input: {sample_string_2}")
    print(f"Output: {result_2}")
    sample_string_3 = "Python"
    separator.split_string(sample_string_3)
    result_3 = separator.get_separated_chars()
    print(f"Input: {sample_string_3}")
    print(f"Output: {result_3}")