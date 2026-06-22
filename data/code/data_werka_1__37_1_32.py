class StringManipulator:
    DEFAULT_STRING1 = "Hello"
    DEFAULT_STRING2 = "World"

    def __init__(self, string1=DEFAULT_STRING1, string2=DEFAULT_STRING2):
        self.string1 = string1
        self.string2 = string2

    @staticmethod
    def concatenate(str1, str2):
        return str1 + str2

    def combine_strings(self):
        return StringManipulator.concatenate(self.string1, self.string2)

if __name__ == '__main__':
    manipulator = StringManipulator()
    result = manipulator.combine_strings()
    print(result)