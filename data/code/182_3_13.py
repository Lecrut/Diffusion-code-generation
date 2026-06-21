class StringSeparator:
    def __init__(self, input_string):
        self.input_string = input_string

    def separate_characters(self):
        return ', '.join(self.input_string)

if __name__ == '__main__':
    separator_instance = StringSeparator("Hello World")
    print(separator_instance.separate_characters())