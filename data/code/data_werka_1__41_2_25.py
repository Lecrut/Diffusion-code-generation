class StringCaseManipulator:
    def __init__(self):
        self.case_methods = {
            'lower': str.lower,
            'upper': str.upper,
            'title': str.title
        }

    def transform(self, text, case_type='lower'):
        if case_type in self.case_methods:
            return self.case_methods[case_type](text)
        else:
            raise ValueError("Invalid case type")

if __name__ == '__main__':
    manipulator = StringCaseManipulator()
    sample_string = "Hello World This Is A Test"
    
    print("Original:", sample_string)
    print("Lowercase:", manipulator.transform(sample_string, 'lower'))
    print("Uppercase:", manipulator.transform(sample_string, 'upper'))
    print("Title Case:", manipulator.transform(sample_string, 'title'))