class StringProcessor:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def get_first_alpha(self):
        for char in self.input_string:
            if char.isalpha():
                return char
        return ""

if __name__ == '__main__':
    sample_strings = ["!@#abc", "123456", "no leading numbers", " ", ""]
    results = [StringProcessor(s).get_first_alpha() for s in sample_strings]
    print(results)