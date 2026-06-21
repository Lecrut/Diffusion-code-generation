class StringOrdMapper:
    def map_to_ord(self, input_string):
        return [ord(c) for c in input_string]

if __name__ == '__main__':
    mapper = StringOrdMapper()
    sample_string = "Hello, World!"
    result = mapper.map_to_ord(sample_string)
    print(result)