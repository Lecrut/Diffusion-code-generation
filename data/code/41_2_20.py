class StringCaseManipulator:
    def transform(self, text):
        return {
            'lower': text.lower(),
            'upper': text.upper(),
            'title': text.title()
        }

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_text = "Hello World"
    result = manipulator.transform(sample_text)
    print(result)