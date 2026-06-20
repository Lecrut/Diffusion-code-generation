class TextProcessor:
    def __init__(self, original_text):
        self.original_text = original_text
        self.transformed_text = ""

    def convert_spaces_to_underscores(self):
        chars = list(self.original_text)
        for i in range(len(chars)):
            if chars[i] == ' ':
                chars[i] = '_'
        self.transformed_text = "".join(chars)
        return self.transformed_text

    def get_original(self):
        return self.original_text

    def get_transformed(self):
        return self.transformed_text

if __name__ == '__main__':
    sample_input = "convert spaces to underscores here"
    processor = TextProcessor(sample_input)
    transformed_result = processor.convert_spaces_to_underscores()
    original_val = processor.get_original()
    final_val = processor.get_transformed()
    print(transformed_result)
    print(original_val)
    print(final_val)