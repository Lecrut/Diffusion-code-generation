class StringUtility:
    @staticmethod
    def calculate_length(input_string):
        return len(input_string)

if __name__ == '__main__':
    sample_values = ["Hello, World!", "Python", "", "OpenAI"]
    for value in sample_values:
        length = StringUtility.calculate_length(value)
        print(f"The length of '{value}' is {length}.")