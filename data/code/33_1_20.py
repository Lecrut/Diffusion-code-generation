class StringProcessor:
    def remove_spaces(self, input_string):
        return ''.join(input_string.split())

if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World from Alibaba Cloud"
    result = processor.remove_spaces(sample_input)
    print(result)