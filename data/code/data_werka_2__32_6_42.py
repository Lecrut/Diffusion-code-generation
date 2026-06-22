class StringProcessor:
    @staticmethod
    def validate_input(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")

    @staticmethod
    def calculate_length(s):
        StringProcessor.validate_input(s)
        return len(s)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    try:
        length = StringProcessor.calculate_length(sample_string)
        print(length)
    except ValueError as e:
        print(e)