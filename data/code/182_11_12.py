class StringSplitter:
    @staticmethod
    def split_to_characters(input_string):
        return list(input_string)

if __name__ == '__main__':
    sample_string = "Hello World"
    result = StringSplitter.split_to_characters(sample_string)
    print(result)