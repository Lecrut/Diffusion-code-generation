class PhraseLengthCalculator:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_phrase_length(self):
        return len(self.input_string.strip())

if __name__ == '__main__':
    sample_values = [
        "",
        "   ",
        "Hello, World!",
        "  Leading and trailing spaces  ",
        "\tTabs\tand\nnewlines\n",
        "Multiple     spaces"
    ]
    
    for value in sample_values:
        calculator = PhraseLengthCalculator(value)
        print(calculator.get_phrase_length())