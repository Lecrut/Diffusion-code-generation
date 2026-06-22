class StringFormatter:
    DELIMITER = ", "

    @staticmethod
    def format_string(s):
        original = s
        all_caps = s.upper()
        sentence_case = s.capitalize()
        return f"{original}{StringFormatter.DELIMITER}{all_caps}{StringFormatter.DELIMITER}{sentence_case}"

if __name__ == '__main__':
    sample_input = "hello world"
    formatted_output = StringFormatter.format_string(sample_input)
    print(formatted_output)