class CaseManipulator:

    def __init__(self, input_string):
        self.input_string = input_string

    def to_lowercase(self):
        return self.input_string.lower()

    def to_uppercase(self):
        return self.input_string.upper()

    def to_title_case(self):
        return self.input_string.title()

    def manipulate_case(self):
        return {'lowercase': self.to_lowercase(), 'uppercase': self.to_uppercase(), 'title_cased': self.to_title_case()}
if __name__ == '__main__':
    sample_input = 'Hello World Example'
    manipulator = CaseManipulator(sample_input)
    result = manipulator.manipulate_case()
    print(result)
    print(manipulator.to_lowercase())
    print(manipulator.to_uppercase())
    print(manipulator.to_title_case())