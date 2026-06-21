class StringToCharList:
    @staticmethod
    def convert_string_to_chars(input_string):
        return list(input_string)

if __name__ == '__main__':
    sample_string_1 = "hello"
    result_1 = StringToCharList.convert_string_to_chars(sample_string_1)
    print(f"Input: {sample_string_1}")
    print(f"Characters: {result_1}")

    sample_string_2 = "world"
    result_2 = StringToCharList.convert_string_to_chars(sample_string_2)
    print(f"Input: {sample_string_2}")
    print(f"Characters: {result_2}")