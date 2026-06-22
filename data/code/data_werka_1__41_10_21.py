class StringManipulator:
    def __init__(self, text):
        self.text = str(text)

    def to_lower(self):
        return self.text.lower()

    def to_upper(self):
        return self.text.upper()

    def to_title(self):
        return self.text.title()

    def swap_case(self):
        return self.text.swapcase()

if __name__ == '__main__':
    sample_text = "Hello World"
    manipulator = StringManipulator(sample_text)
    
    print("Original:", sample_text)
    print("Lower:", manipulator.to_lower())
    print("Upper:", manipulator.to_upper())
    print("Title:", manipulator.to_title())
    print("Swap:", manipulator.swap_case())