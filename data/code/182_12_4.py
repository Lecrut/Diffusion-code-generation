class StringSeparator:
    def __init__(self):
        self._separated_chars = []
    def split_string(self, input_string):
        self._separated_chars = list(input_string)
    def get_separated_string(self):
        return "".join(self._separated_chars)
if __name__ == '__main__':
    separator = StringSeparator()
    sample_string_1 = "hello"
    separator.split_string(sample_string_1)
    print(f"Original string: {sample_string_1}")
    print(f"Separated characters (as list): {separator._separated_chars}")
    print(f"Rejoined string: {separator.get_separated_string()}")
    sample_string_2 = "world"
    separator.split_string(sample_string_2)
    print(f"\nOriginal string: {sample_string_2}")
    print(f"Separated characters (as list): {separator._separated_chars}")
    print(f"Rejoined string: {separator.get_separated_string()}")