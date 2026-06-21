class StringSeparator:
    SEPARATOR = ','

    @staticmethod
    def separate(input_string):
        return StringSeparator.SEPARATOR.join(input_string)

if __name__ == '__main__':
    sample_string = "PythonProgramming"
    print(StringSeparator.separate(sample_string))