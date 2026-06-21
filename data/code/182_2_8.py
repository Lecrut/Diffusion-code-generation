class StringConverter:
    def __init__(self, s):
        self.string = s

    def convert_to_char_list(self):
        return list(self.string)

if __name__ == '__main__':
    converter = StringConverter("Hello, World!")
    print(converter.convert_to_char_list())