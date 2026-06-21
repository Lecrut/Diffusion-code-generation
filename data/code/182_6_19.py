class CharacterSeparator:
    @staticmethod
    def separate_chars_by_ord(input_string):
        return [ord(char) for char in input_string]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = CharacterSeparator.separate_chars_by_ord(sample_string)
    print(result)