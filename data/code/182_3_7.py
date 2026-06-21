class StringSeparator:
    def separate_characters(self, input_string):
        return ', '.join(input_string)

if __name__ == '__main__':
    separator = StringSeparator()
    result = separator.separate_characters("Hello World")
    print(result)