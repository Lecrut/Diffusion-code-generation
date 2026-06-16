class StringProcessor:
    def convert_to_lower(self, text: str) -> str:
        return text.lower()
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string1 = "HeLlO WoRlD"
    sample_string2 = "PYTHON Programming"
    print(f"'{sample_string1}' converted to lower: '{processor.convert_to_lower(sample_string1)}'")
    print(f"'{sample_string2}' converted to lower: '{processor.convert_to_lower(sample_string2)}'")