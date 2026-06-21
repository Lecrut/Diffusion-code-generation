class StringToOrdConverter:
    def convert_string_to_ord(self, input_string):
        return [ord(c) for c in input_string]

if __name__ == '__main__':
    converter = StringToOrdConverter()
    sample_string = "Hello, World!"
    result = converter.convert_string_to_ord(sample_string)
    print(result)