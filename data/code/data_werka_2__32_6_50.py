class StringOperations:
    @staticmethod
    def validate_string(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")

    @staticmethod
    def compute_length(s):
        StringOperations.validate_string(s)
        return len(s)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud Qwen"
    try:
        result_length = StringOperations.compute_length(sample_input)
        print(f"The length of the input string is: {result_length}")
    except ValueError as e:
        print(e)