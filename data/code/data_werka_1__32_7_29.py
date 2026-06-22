class StringUtility:
    @staticmethod
    def calculate_length(input_string):
        return len(input_string)

if __name__ == '__main__':
    sample_values = ["hello", "world", "Python", "programming"]
    for value in sample_values:
        print(StringUtility.calculate_length(value))