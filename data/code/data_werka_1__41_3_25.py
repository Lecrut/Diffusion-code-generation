class StringTransformer:
    @staticmethod
    def transform(input_str):
        lowercase_str = input_str.lower()
        reversed_case_str = input_str.swapcase()
        return (input_str, lowercase_str, reversed_case_str)

if __name__ == '__main__':
    sample_string = "Python Programming"
    result = StringTransformer.transform(sample_string)
    print(result)