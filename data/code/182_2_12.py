class StringConverter:
    def __init__(self, string):
        self.string = string

    def to_char_list(self):
        return list(self.string)

if __name__ == '__main__':
    converter = StringConverter("hello world")
    char_list = converter.to_char_list()
    print(char_list)