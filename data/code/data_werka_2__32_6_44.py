class StringMetrics:
    @staticmethod
    def is_valid_string(s):
        return isinstance(s, str)

    @staticmethod
    def calculate_length(s):
        if not StringMetrics.is_valid_string(s):
            raise ValueError("Input must be a string")
        return len(s)

if __name__ == '__main__':
    sample_string = "Welcome to Alibaba Cloud!"
    try:
        length_of_string = StringMetrics.calculate_length(sample_string)
        print(f"Length of '{sample_string}': {length_of_string}")
    except ValueError as e:
        print(e)