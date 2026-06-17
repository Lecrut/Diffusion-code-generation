class StringProcessor:
    def convert_to_lower(self, text: str) -> str:
        return text.lower()
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string1 = "HeLlO WoRlD"
    sample_string2 = "PYTHON"
    sample_string3 = "aBcDeFg"
    result1 = processor.convert_to_lower(sample_string1)
    result2 = processor.convert_to_lower(sample_string2)
    result3 = processor.convert_to_lower(sample_string3)
    print(f"'{sample_string1}' converted to lower: '{result1}'")
    print(f"'{sample_string2}' converted to lower: '{result2}'")
    print(f"'{sample_string3}' converted to lower: '{result3}'")