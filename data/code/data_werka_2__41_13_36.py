class StringTransformer:
    def __init__(self, input_string):
        self.input_string = input_string

    def to_lowercase(self):
        return self.input_string.lower()

    def swap_case(self):
        lowercased = self.to_lowercase()
        return lowercased.swapcase()

if __name__ == '__main__':
    test_value = 'Hello World'
    transformer = StringTransformer(test_value)
    result1 = transformer.to_lowercase()
    result2 = transformer.swap_case()
    print(result1)
    print(result2)