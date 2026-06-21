class StringManipulator:
    def __init__(self, input_string):
        self.input_string = input_string

    @staticmethod
    def convert_to_lowercase(input_string):
        return input_string.lower()

    @staticmethod
    def convert_to_uppercase(input_string):
        return input_string.upper()

    @staticmethod
    def convert_to_title_case(input_string):
        return input_string.title()

    @staticmethod
    def swap_case(input_string):
        return input_string.swapcase()

if __name__ == '__main__':
    sample_string = "Hello, World!"
    manipulator = StringManipulator(sample_string)
    
    print(StringManipulator.convert_to_lowercase(sample_string))
    print(StringManipulator.convert_to_uppercase(sample_string))
    print(StringManipulator.convert_to_title_case(sample_string))
    print(StringManipulator.swap_case(sample_string))