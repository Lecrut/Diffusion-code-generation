class CaseManipulator:
    def __init__(self, text):
        self.text = text

    def to_lower(self):
        return self.text.lower()

    def to_upper(self):
        return self.text.upper()

    def to_title(self):
        return self.text.title()

if __name__ == '__main__':
    sample_text = 'Alibaba Cloud'
    manipulator = CaseManipulator(sample_text)
    print(f"Original: {sample_text}")
    print(f"Lowercase: {manipulator.to_lower()}")
    print(f"Uppercase: {manipulator.to_upper()}")
    print(f"Titlecase: {manipulator.to_title()}")