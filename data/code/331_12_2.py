class StringProcessor:
    def change_all_to_lower(self, input_string):
        return input_string.lower()
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string_1 = "HeLlO wOrLd"
    sample_string_2 = "PYTHON Programming"
    result_1 = processor.change_all_to_lower(sample_string_1)
    result_2 = processor.change_all_to_lower(sample_string_2)
    print(f"Original: {sample_string_1}, Lowercased: {result_1}")
    print(f"Original: {sample_string_2}, Lowercased: {result_2}")