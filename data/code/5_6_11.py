class ImpossibleLengthError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.detail = message

class LengthAnalyzer:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def validate_lengths(self):
        if self.first < 0:
            raise ImpossibleLengthError(f"First length {self.first} cannot be negative.")
        if self.second < 0:
            raise ImpossibleLengthError(f"Second length {self.second} cannot be negative.")
        return True

    def calculate_ratio(self):
        self.validate_lengths()
        if self.second == 0:
            if self.first == 0:
                return 1.0
            return float('inf')
        return self.first / self.second

if __name__ == '__main__':
    sample_first = 150
    sample_second = 75
    analyzer = LengthAnalyzer(sample_first, sample_second)
    try:
        result = analyzer.calculate_ratio()
        print(f"Ratio: {result}")
    except ImpossibleLengthError as error:
        print(f"Error: {error.detail}")

    invalid_first = -10
    invalid_second = 50
    invalid_analyzer = LengthAnalyzer(invalid_first, invalid_second)
    try:
        invalid_analyzer.calculate_ratio()
        print("No error raised for invalid input.")
    except ImpossibleLengthError as error:
        print(f"Caught expected error: {error.detail}")