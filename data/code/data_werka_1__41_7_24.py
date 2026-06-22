class StringFormatter:
    @staticmethod
    def format_string(s):
        original = s
        all_caps = s.upper()
        sentence_case = s.capitalize()
        return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_values = ["hello world", "python programming", "list of strings"]
    formatted_strings = [StringFormatter.format_string(s) for s in sample_values]
    print(formatted_strings)