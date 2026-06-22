class StringCaseManipulator:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.text = text

    def to_lower(self):
        return self.text.lower()

    def to_upper(self):
        return self.text.upper()

    def to_title(self):
        return self.text.title()

if __name__ == '__main__':
    sample_text = 'Hello World'
    try:
        manipulator = StringCaseManipulator(sample_text)
        print("Original:", sample_text)
        print("Lowercase:", manipulator.to_lower())
        print("Uppercase:", manipulator.to_upper())
        print("Titlecase:", manipulator.to_title())
    except ValueError as e:
        print(e)