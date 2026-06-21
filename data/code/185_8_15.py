import re

class NumberExtractor:
    NUMERIC_PATTERN = r'-?\d+\.\d+|\d+'

    @staticmethod
    def extract_numbers(text):
        return [float(num) for num in re.findall(NumberExtractor.NUMERIC_PATTERN, text)]

if __name__ == '__main__':
    sample_text = "There are 42 apples and 3.14159 pi."
    print(NumberExtractor.extract_numbers(sample_text))