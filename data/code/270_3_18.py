class StringModifier:
    @staticmethod
    def remove_spaces(input_string):
        return input_string.replace(' ', '')

if __name__ == '__main__':
    sample_string = '  Hello World! This is a test.'
    result = StringModifier.remove_spaces(sample_string)
    print(result)