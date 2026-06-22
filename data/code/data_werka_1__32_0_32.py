class PhraseLengthCalculator:
    @staticmethod
    def calculate_phrase_length(phrase):
        return len(phrase)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    calculator = PhraseLengthCalculator()
    print(calculator.calculate_phrase_length(sample_text))