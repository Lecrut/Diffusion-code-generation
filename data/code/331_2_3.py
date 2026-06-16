class StringProcessor:
    def convert_to_lower(self, text: str) -> str:
        return text.lower()
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = "HeLlO WoRlD"
    sample_string_2 = "PYTHON Programming"
    sample_string_3 = "already lower"
    result_1 = processor.convert_to_lower(sample_string_1)
    result_2 = processor.convert_to_lower(sample_string_2)
    result_3 = processor.convert_to_lower(sample_string_3)
    print(f"'{sample_string_1}' converted to lower: '{result_1}'")
    print(f"'{sample_string_2}' converted to lower: '{result_2}'")
    print(f"'{sample_string_3}' converted to lower: '{result_3}'")