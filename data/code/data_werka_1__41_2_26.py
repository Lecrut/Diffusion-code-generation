class StringCaseManipulator:
    def transform(self, text):
        return {
            'lowercase': self.to_lowercase(text),
            'uppercase': self.to_uppercase(text),
            'titlecase': self.to_titlecase(text)
        }

    def to_lowercase(self, text):
        return text.lower()

    def to_uppercase(self, text):
        return text.upper()

    def to_titlecase(self, text):
        return text.title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_text = "Hello World"
    result = manipulator.transform(sample_text)
    print(result)