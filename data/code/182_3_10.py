class StringSeparator:
    def separate(self, input_string):
        return ', '.join(input_string)

if __name__ == '__main__':
    separator = StringSeparator()
    sample_string = "Hello World"
    print(separator.separate(sample_string))