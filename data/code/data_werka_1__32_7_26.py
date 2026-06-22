class LengthCalculator:
    @staticmethod
    def calculate_length(input_string):
        return len(input_string)

if __name__ == '__main__':
    sample_values = ["hello", "world", "Python", "programming"]
    for value in sample_values:
        length = LengthCalculator.calculate_length(value)
        print(f"The length of '{value}' is {length}.")