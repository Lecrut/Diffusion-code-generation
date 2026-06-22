class StringFormatter:
    def __init__(self, original_string):
        self.original_string = original_string

    def to_all_caps(self):
        return self.original_string.upper()

    def to_sentence_case(self):
        return self.original_string.capitalize()

    def formatted_output(self):
        all_caps = self.to_all_caps()
        sentence_case = self.to_sentence_case()
        return f"{self.original_string}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_string = "hello world"
    formatter = StringFormatter(sample_string)
    print(formatter.formatted_output())