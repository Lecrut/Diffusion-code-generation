class StringManipulator:
    LOWER = 'lower'
    UPPER = 'upper'
    TITLE = 'title'
    SWAP = 'swap'

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
    sample_text = "Hello World"
    manipulator = StringManipulator(sample_text)
    
    print(f"Original: {sample_text}")
    print(f"Lowercase: {manipulator.to_lowercase()}")
    print(f"Uppercase: {manipulator.to_uppercase()}")
    print(f"Title Case: {manipulator.to_title_case()}")
    print(f"Swap Case: {manipulator.swap_case()}")