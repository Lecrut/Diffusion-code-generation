class StringManipulator:
    def __init__(self):
        self.s1 = "Hello"
        self.s2 = "World"

    def combine_strings(self):
        return f"{self.s1} {self.s2}"

if __name__ == '__main__':
    manipulator = StringManipulator()
    result = manipulator.combine_strings()
    print(result)