class StringManipulator:
    LOWER = 'lower'
    UPPER = 'upper'
    TITLE = 'title'
    SWAP = 'swap'

    def to_lowercase(self, text):
        return text.lower()

    def to_uppercase(self, text):
        return text.upper()

    def to_titlecase(self, text):
        return text.title()

    def swap_case(self, text):
        return text.swapcase()

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_text = "Hello World"
    
    print(f"Original: '{sample_text}'")
    print(f"Lowercase: {manipulator.to_lowercase(sample_text)}")
    print(f"Uppercase: {manipulator.to_uppercase(sample_text)}")
    print(f"Title Case: {manipulator.to_titlecase(sample_text)}")
    print(f"Swap Case: {manipulator.swap_case(sample_text)}")