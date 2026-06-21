def phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

class StringLengthCalculator:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def calculate_length(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    try:
        print(phrase_length(sample_phrase))
        calculator = StringLengthCalculator(sample_phrase)
        print(calculator.calculate_length())
    except ValueError as e:
        print(e)