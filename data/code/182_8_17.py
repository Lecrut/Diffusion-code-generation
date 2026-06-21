class StringSeparator:
    def separate(self, input_string):
        return [(i, char) for i, char in enumerate(input_string)]

if __name__ == '__main__':
    separator = StringSeparator()
    sample_string = "Hello World"
    print("Original string:", sample_string)
    result = separator.separate(sample_string)
    print("Separated characters with indices:", result)