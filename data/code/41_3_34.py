class StringTransformer:
    def __init__(self, input_str):
        self.original = input_str

    def to_lowercase(self):
        return self.original.lower()

    def reverse_case(self):
        return self.original.swapcase()

    def transform(self):
        return (self.original, self.to_lowercase(), self.reverse_case())

if __name__ == '__main__':
    sample_string = "Hello World"
    transformer = StringTransformer(sample_string)
    print(transformer.transform())