class StringProcessor:
    @staticmethod
    def remove_spaces(input_string):
        return "".join(char for char in input_string if char != " ")

if __name__ == '__main__':
    sample_input = "Python programming is fun!"
    print(StringProcessor.remove_spaces(sample_input))