class StringSeparator:
    def __init__(self):
        self._separated_chars = []
    def split_string(self, input_string):
        self._separated_chars = list(input_string)
    def get_separated_chars(self):
        return self._separated_chars
if __name__ == '__main__':
    separator = StringSeparator()
    sample_string = "HelloWorld"
    separator.split_string(sample_string)
    result = separator.get_separated_chars()
    print(result)