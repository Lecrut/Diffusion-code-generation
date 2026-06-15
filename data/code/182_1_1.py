class StringSeparator:
    def split_string(self, input_string):
        return list(input_string)
if __name__ == '__main__':
    separator = StringSeparator()
    sample_string1 = "hello"
    result1 = separator.split_string(sample_string1)
    print(f"Input: {sample_string1}")
    print(f"Output: {result1}")
    sample_string2 = "world"
    result2 = separator.split_string(sample_string2)
    print(f"Input: {sample_string2}")
    print(f"Output: {result2}")
    sample_string3 = "Python"
    result3 = separator.split_string(sample_string3)
    print(f"Input: {sample_string3}")
    print(f"Output: {result3}")