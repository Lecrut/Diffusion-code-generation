class StringManipulator:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    def combine_strings(self):
        return self.str1 + self.str2
if __name__ == '__main__':
    s1 = "Hello"
    s2 = "World"
    manipulator = StringManipulator(s1, s2)
    result = manipulator.combine_strings()
    print(result)