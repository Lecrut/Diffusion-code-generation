class StringOperations:
    @staticmethod
    def is_valid_string(s):
        return isinstance(s, str)

    @staticmethod
    def calculate_length(s):
        if not StringOperations.is_valid_string(s):
            raise ValueError("Input must be a string")
        return len(s)

if __name__ == '__main__':
    sample_input = "Welcome to Alibaba Cloud!"
    try:
        length_of_sample = StringOperations.calculate_length(sample_input)
        print(f"Length of the input string: {length_of_sample}")
    except ValueError as e:
        print(e)