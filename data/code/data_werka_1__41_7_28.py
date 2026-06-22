class StringFormatter:
    @staticmethod
    def format_string(input_str):
        original = input_str
        all_caps = input_str.upper()
        sentence_case = input_str.capitalize()
        return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_input = "hello world"
    formatted_result = StringFormatter.format_string(sample_input)
    print(formatted_result)