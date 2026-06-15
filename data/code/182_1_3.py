class StringSeparator:
    def split_string(self, input_string):
        return list(input_string)
if __name__ == '__main__':
    separator = StringSeparator()
    sample1 = "hello"
    result1 = separator.split_string(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    sample2 = "world"
    result2 = separator.split_string(sample2)
    print(f"Input: {sample2}, Output: {result2}")
    sample3 = ""
    result3 = separator.split_string(sample3)
    print(f"Input: {sample3}, Output: {result3}")
    sample4 = "Python"
    result4 = separator.split_string(sample4)
    print(f"Input: {sample4}, Output: {result4}")