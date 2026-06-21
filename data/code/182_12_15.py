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
    print(f"Separated Characters: {result_1}")

    separator.split_string("world")
    result_2 = separator.get_separated_chars()
    print(f"Input: world")
    print(f"Separated Characters: {result_2}")