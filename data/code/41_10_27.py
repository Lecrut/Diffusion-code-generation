class StringManipulator:
    def __init__(self, text):
        self.text = str(text)

    def to_lowercase(self):
        return self.text.lower()

    def to_uppercase(self):
        return self.text.upper()

    def to_title_case(self):
        return self.text.title()

    def swap_case(self):
        return self.text.swapcase()

if __name__ == '__main__':
    sample1 = "Hello World"
    manipulator1 = StringManipulator(sample1)
    print(manipulator1.to_lowercase())
    print(manipulator1.to_uppercase())

    sample2 = "PYTHON FUNCTION"
    manipulator2 = StringManipulator(sample2)
    print(manipulator2.to_title_case())

    sample3 = "MiXeD CaSe"
    manipulator3 = StringManipulator(sample3)
    print(manipulator3.swap_case())