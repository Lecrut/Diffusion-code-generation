def calculate_length(phrase):
    return len(phrase)

class StringLengthCalculator:
    def __init__(self, phrase):
        self.phrase = phrase
    def get_phrase_length(self):
        return len(self.phrase)

if __name__ == '__main__':
    sample_input = "Python Programming"
    length_function_result = calculate_length(sample_input)
    print(f"Length using function: {length_function_result}")

    calculator_instance = StringLengthCalculator(sample_input)
    length_method_result = calculator_instance.get_phrase_length()
    print(f"Length using class method: {length_method_result}")