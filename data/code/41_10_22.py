class StringManipulator:
    def __init__(self, text):
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def to_uppercase(self):
        return self.text.upper()

    def to_title_case(self):
        return self.text.title()

    def swap_case(self):
        return self.text.swapcase()

if __name__ == '__main__':
    sample_text = "Hello, World!"
    manipulator = StringManipulator(sample_text)
    
    print(manipulator.to_lowercase())
    print(manipulator.to_uppercase())
    print(manipulator.to_title_case())
    print(manipulator.swap_case())