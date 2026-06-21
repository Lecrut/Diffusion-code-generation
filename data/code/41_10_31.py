class StringManipulator:
    LOWERCASE_CONVERSION = 'lower'
    UPPERCASE_CONVERSION = 'upper'
    TITLECASE_CONVERSION = 'title'
    SWAPCASE_CONVERSION = 'swap'

    def __init__(self, input_string):
        self.input_string = input_string

    def convert(self, conversion_type):
        if conversion_type == self.LOWERCASE_CONVERSION:
            return self.to_lowercase()
        elif conversion_type == self.UPPERCASE_CONVERSION:
            return self.to_uppercase()
        elif conversion_type == self.TITLECASE_CONVERSION:
            return self.to_title_case()
        elif conversion_type == self.SWAPCASE_CONVERSION:
            return self.swap_case()
        else:
            raise ValueError("Unsupported conversion type")

    def to_lowercase(self):
        return self.input_string.lower()

    def to_uppercase(self):
        return self.input_string.upper()

    def to_title_case(self):
        return self.input_string.title()

    def swap_case(self):
        return self.input_string.swapcase()

if __name__ == '__main__':
    sample_string = "Hello, World!"
    manipulator = StringManipulator(sample_string)
    
    print("Lowercase:", manipulator.convert(StringManipulator.LOWERCASE_CONVERSION))
    print("Uppercase:", manipulator.convert(StringManipulator.UPPERCASE_CONVERSION))
    print("Title Case:", manipulator.convert(StringManipulator.TITLECASE_CONVERSION))
    print("Swap Case:", manipulator.convert(StringManipulator.SWAPCASE_CONVERSION))