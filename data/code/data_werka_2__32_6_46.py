class StringMetrics:
    @staticmethod
    def validate_input(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")

    @staticmethod
    def calculate_length(s):
        StringMetrics.validate_input(s)
        return len(s)

if __name__ == '__main__':
    sample_strings = ["Alibaba Cloud", "Innovative Solutions", 12345]
    for sample in sample_strings:
        try:
            length = StringMetrics.calculate_length(sample)
            print(f"Length of '{sample}': {length}")
        except ValueError as e:
            print(e)