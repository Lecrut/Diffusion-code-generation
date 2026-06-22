class StringTransformer:
    REPLACEMENT_CHAR = "_"
    TARGET_CHAR = " "

    @staticmethod
    def replace_spaces(input_text: str) -> str:
        return input_text.replace(
            StringTransformer.TARGET_CHAR,
            StringTransformer.REPLACEMENT_CHAR
        )

if __name__ == '__main__':
    sample_data = "The quick brown fox jumps over the lazy dog"
    transformer = StringTransformer()
    output_result = transformer.replace_spaces(sample_data)
    print(output_result)