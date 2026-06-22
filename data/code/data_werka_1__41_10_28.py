class StringManipulator:
    LOWER = 'lower'
    UPPER = 'upper'
    TITLE = 'title'
    SWAP = 'swap'

    @staticmethod
    def to_lower(text):
        return text.lower()

    @staticmethod
    def to_upper(text):
        return text.upper()

    @staticmethod
    def to_title(text):
        return text.title()

    @staticmethod
    def swap_case(text):
        return text.swapcase()

    def manipulate(self, text, case):
        if case == self.LOWER:
            return self.to_lower(text)
        elif case == self.UPPER:
            return self.to_upper(text)
        elif case == self.TITLE:
            return self.to_title(text)
        elif case == self.SWAP:
            return self.swap_case(text)
        else:
            return text

if __name__ == '__main__':
    manipulator = StringManipulator()
    print(manipulator.manipulate("Hello World", StringManipulator.LOWER))
    print(manipulator.manipulate("PYTHON FUNCTION", StringManipulator.UPPER))
    print(manipulator.manipulate("MiXeD CaSe", StringManipulator.TITLE))
    print(manipulator.manipulate("sWaP cAsE", StringManipulator.SWAP))