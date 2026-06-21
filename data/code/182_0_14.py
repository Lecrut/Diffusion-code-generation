class CharacterSeparator:
    def separate(self, input_string):
        return '-'.join([char for char in input_string])

if __name__ == '__main__':
    separator = CharacterSeparator()
    sample_strings = ["Hello World", "Python", "hello"]
    for string in sample_strings:
        result = separator.separate(string)
        print(result)