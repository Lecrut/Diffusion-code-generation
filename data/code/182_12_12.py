class StringSeparator:
    @staticmethod
    def split_string(input_string):
        return list(input_string)

if __name__ == '__main__':
    sample_string_1 = "hello"
    result_1 = StringSeparator.split_string(sample_string_1)
    print(f"Input: {sample_string_1}")
    print(f"Separated Characters: {result_1}")

    sample_string_2 = "world"
    result_2 = StringSeparator.split_string(sample_string_2)
    print(f"Input: {sample_string_2}")
    print(f"Separated Characters: {result_2}")