class StringManipulator:
    def __init__(self):
        self._string1 = ""
        self._string2 = ""

    @property
    def string1(self):
        return self._string1

    @string1.setter
    def string1(self, value):
        if not isinstance(value, str):
            raise ValueError("string1 must be a string")
        self._string1 = value

    @property
    def string2(self):
        return self._string2

    @string2.setter
    def string2(self, value):
        if not isinstance(value, str):
            raise ValueError("string2 must be a string")
        self._string2 = value

    def combine_strings(self):
        return self.string1 + self.string2

if __name__ == '__main__':
    manipulator = StringManipulator()
    try:
        manipulator.string1 = "Hello"
        manipulator.string2 = "World"
        result = manipulator.combine_strings()
        print(result)
    except ValueError as e:
        print(e)