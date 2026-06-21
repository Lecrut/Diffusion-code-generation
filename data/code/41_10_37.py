class StringManipulator:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

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
    try:
        manipulator = StringManipulator(sample_string)
        print(manipulator.to_lowercase())
        print(manipulator.to_uppercase())
        print(manipulator.to_title_case())
        print(manipulator.swap_case())
    except ValueError as e:
        print(e)