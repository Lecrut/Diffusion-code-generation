import re

class StringModifier:
    @staticmethod
    def remove_spaces(input_string):
        return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    processor = StringModifier()
    sample_input1 = "Hello, World! This is a test."
    sample_input2 = "Python is awesome!"
    print(processor.remove_spaces(sample_input1))
    print(processor.remove_spaces(sample_input2))