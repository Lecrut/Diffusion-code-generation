class StringSeparator:
    def split_string(self, input_string):
        return list(input_string)
if __name__ == '__main__':
    separator = StringSeparator()
    sample_string_1 = "hello"
    result_1 = separator.split_string(sample_string_1)
    print(f"Input: {sample_string_1}")
    print(f"Output: {result_1}")
    sample_string_2 = "world"
    result_2 = separator.split_string(sample_string_2)
    print(f"Input: {sample_string_2}")
    print(f"Output: {result_2}")
    sample_string_3 = "Python"
    result_3 = separator.split_string(sample_string_3)
    print(f"Input: {sample_string_3}")
    print(f"Output: {result_3}")