class StringManipulator:
    def __init__(self, str1, str2):
        self.set_string1(str1)
        self.set_string2(str2)

    def set_string1(self, value):
        if not isinstance(value, str):
            raise ValueError("string1 must be a string")
        self.string1 = value

    def set_string2(self, value):
        if not isinstance(value, str):
            raise ValueError("string2 must be a string")
        self.string2 = value

    def combine_strings(self):
        return self.string1 + self.string2

if __name__ == '__main__':
    try:
        manipulator = StringManipulator("Hello", "World")
        result = manipulator.combine_strings()
        print(result)
    except ValueError as e:
        print(e)