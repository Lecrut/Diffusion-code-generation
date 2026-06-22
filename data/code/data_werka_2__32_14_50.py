def calculate_length(phrase):
    return len(phrase)

class LengthCalculator:
    def __init__(self, phrase):
        self.phrase = phrase
    def compute_length(self):
        return len(self.phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    length_function_result = calculate_length(sample_phrase)
    print(length_function_result)
    
    length_calculator = LengthCalculator(sample_phrase)
    length_method_result = length_calculator.compute_length()
    print(length_method_result)