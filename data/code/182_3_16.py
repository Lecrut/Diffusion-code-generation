class StringSeparator:
    def separate_characters(self, input_string):
        return ', '.join(input_string)

if __name__ == '__main__':
    separator = StringSeparator()
    sample_string = "Hello World"
    print(separator.separate_characters(sample_string))