class StringConverter:
    @staticmethod
    def to_char_list(input_string):
        return list(input_string)

if __name__ == '__main__':
    converter = StringConverter()
    sample_string_1 = "hello"
    result_1 = converter.to_char_list(sample_string_1)
    print(f"Input: {sample_string_1}")
    print(f"Character List: {result_1}")
    sample_string_2 = "world"
    result_2 = converter.to_char_list(sample_string_2)
    print(f"Input: {sample_string_2}")
    print(f"Character List: {result_2}")