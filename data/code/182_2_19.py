class StringConverter:
    @staticmethod
    def string_to_char_list(s):
        return list(s)

if __name__ == '__main__':
    converter = StringConverter()
    sample_string = "Hello, World!"
    char_list = converter.string_to_char_list(sample_string)
    print(char_list)