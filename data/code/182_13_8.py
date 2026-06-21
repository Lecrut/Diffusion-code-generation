class StringSeparator:
    SEPARATOR = ','
    
    @staticmethod
    def separate(input_string):
        return StringSeparator.SEPARATOR.join(input_string)

if __name__ == '__main__':
    separator_instance = StringSeparator()
    sample_string = "PythonProgramming"
    result = separator_instance.separate(sample_string)
    print(result)