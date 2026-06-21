class StringLengthCalculator:
    MAX_STRING_LENGTH = 1000

    @staticmethod
    def calculate_phrase_length(phrase):
        if not isinstance(phrase, str):
            raise ValueError("Input must be a string")
        if len(phrase) > StringLengthCalculator.MAX_STRING_LENGTH:
            raise ValueError("String length exceeds maximum allowed limit")
        return len(phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(StringLengthCalculator.calculate_phrase_length(sample_phrase))