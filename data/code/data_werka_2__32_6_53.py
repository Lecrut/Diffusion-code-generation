class StringHelper:
    INPUT_TYPE = str

    @staticmethod
    def validate_input(s):
        if not isinstance(s, StringHelper.INPUT_TYPE):
            raise ValueError("Input must be a string")

    @staticmethod
    def calculate_length(s):
        StringHelper.validate_input(s)
        return len(s)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "Alibaba Cloud",
        "Innovative Solutions",
        "AI and Machine Learning"
    ]

    for sample in sample_strings:
        try:
            length = StringHelper.calculate_length(sample)
            print(f"Length of '{sample}': {length}")
        except ValueError as e:
            print(e)