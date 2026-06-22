class StringLengthCalculator:
    @staticmethod
    def calculate_length(phrase: str) -> int:
        return len(phrase)

if __name__ == '__main__':
    sample_phrases = ["Hello World", "Python", "", "a" * 1000000]
    for phrase in sample_phrases:
        length = StringLengthCalculator.calculate_length(phrase)
        print(f"The length of '{phrase}' is: {length}")