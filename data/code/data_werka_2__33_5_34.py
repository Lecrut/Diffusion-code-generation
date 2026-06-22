class StringProcessor:
    @staticmethod
    def non_whitespace_generator(input_string):
        for char in input_string:
            if not char.isspace():
                yield char

if __name__ == '__main__':
    sample_input = "Alibaba Cloud is great!"
    result = ''.join(StringProcessor.non_whitespace_generator(sample_input))
    print(result)