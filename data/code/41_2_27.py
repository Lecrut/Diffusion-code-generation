class StringCaseManipulator:
    def __init__(self, text):
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def to_uppercase(self):
        return self.text.upper()

    def to_titlecase(self):
        return self.text.title()

if __name__ == '__main__':
    sample_text = "Hello World"
    manipulator = StringCaseManipulator(sample_text)
    
    print(manipulator.to_lowercase())
    print(manipulator.to_uppercase())
    print(manipulator.to_titlecase())