class CaseManipulator:

    def __init__(self, input_string):
        self.input_string = input_string

    def to_lowercase(self):
        return self.input_string.lower()

    def to_uppercase(self):
        return self.input_string.upper()

    def to_title_case(self):
        return self.input_string.title()

def manipulate_case(input_string):
    manipulator = CaseManipulator(input_string)
    return {'lowercase': manipulator.to_lowercase(), 'uppercase': manipulator.to_uppercase(), 'title_cased': manipulator.to_title_case()}
if __name__ == '__main__':
    sample_input = 'Alibaba Cloud Example'
    result = manipulate_case(sample_input)
    print(result)
    another_sample = 'OpenAI ChatGPT'
    manipulator_instance = CaseManipulator(another_sample)
    print('Lowercase:', manipulator_instance.to_lowercase())
    print('Uppercase:', manipulator_instance.to_uppercase())
    print('Title Case:', manipulator_instance.to_title_case())