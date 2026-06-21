class StringManipulator:

    def to_lowercase(self, s):
        return s.lower()

    def to_uppercase(self, s):
        return s.upper()

    def to_title_case(self, s):
        return s.title()

    def swap_case(self, s):
        return s.swapcase()
if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_string = 'Hello World!'
    print(manipulator.to_lowercase(sample_string))
    print(manipulator.to_uppercase(sample_string))
    print(manipulator.to_title_case(sample_string))
    print(manipulator.swap_case(sample_string))