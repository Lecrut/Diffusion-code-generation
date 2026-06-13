class StringUtils:
    @staticmethod
    def split_string_into_words(text: str) -> list[str]:
        return text.split()
if __name__ == '__main__':
    sample_string_1 = "This is a sample string"
    result_1 = StringUtils.split_string_into_words(sample_string_1)
    print(f"Input: '{sample_string_1}'")
    print(f"Output: {result_1}")
    sample_string_2 = "  leading and trailing spaces "
    result_2 = StringUtils.split_string_into_words(sample_string_2)
    print(f"Input: '{sample_string_2}'")
    print(f"Output: {result_2}")
    sample_string_3 = "singleword"
    result_3 = StringUtils.split_string_into_words(sample_string_3)
    print(f"Input: '{sample_string_3}'")
    print(f"Output: {result_3}")
    sample_string_4 = ""
    result_4 = StringUtils.split_string_into_words(sample_string_4)
    print(f"Input: '{sample_string_4}'")
    print(f"Output: {result_4}")