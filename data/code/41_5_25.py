class StringCaseManipulator:

    def __init__(self, text):
        self.text = text

    def to_lower(self):
        return self.text.lower()

    def to_upper(self):
        return self.text.upper()

    def to_title(self):
        return self.text.title()
if __name__ == '__main__':
    sample_text = 'hello world'
    manipulator = StringCaseManipulator(sample_text)
    print(manipulator.to_lower())
    print(manipulator.to_upper())
    print(manipulator.to_title())