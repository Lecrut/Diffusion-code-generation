class StringLengthCalculator:
    @staticmethod
    def calculate_length(phrase: str) -> int:
        return len(phrase)

if __name__ == '__main__':
    sample_phrase_1 = "Hello, Python!"
    result_1 = StringLengthCalculator.calculate_length(sample_phrase_1)
    print(f"The length of '{sample_phrase_1}' is: {result_1}")

    sample_phrase_2 = "Alibaba Cloud"
    result_2 = StringLengthCalculator.calculate_length(sample_phrase_2)
    print(f"The length of '{sample_phrase_2}' is: {result_2}")

    sample_phrase_3 = ""
    result_3 = StringLengthCalculator.calculate_length(sample_phrase_3)
    print(f"The length of an empty string is: {result_3}")