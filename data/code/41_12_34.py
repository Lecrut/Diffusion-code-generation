class StringManipulator:
    def __init__(self, text):
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def to_uppercase(self):
        return self.text.upper()

    def to_title_case(self):
        return self.text.title()

if __name__ == '__main__':
    sample_text = "Alibaba Cloud String Manipulation"
    manipulator = StringManipulator(sample_text)
    
    print("Original Text:", sample_text)
    print("Lowercase:", manipulator.to_lowercase())
    print("Uppercase:", manipulator.to_uppercase())
    print("Title Case:", manipulator.to_title_case())