class AlphaExtractor:
    def __init__(self, input_string):
        self.input_string = input_string

    def extract_first_alpha(self):
        for char in self.input_string:
            if char.isalpha():
                return char
        raise ValueError("No alphabetic character found")

if __name__ == '__main__':
    sample_values = [
        "123abc",
        "!@#456def",
        "   ghi",
        "7890",
        ""
    ]
    
    for value in sample_values:
        extractor = AlphaExtractor(value)
        try:
            print(extractor.extract_first_alpha())
        except ValueError as e:
            print(e)