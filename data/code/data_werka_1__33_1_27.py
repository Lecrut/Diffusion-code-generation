class StringProcessor:
    def remove_spaces(self, input_string):
        result = []
        for char in input_string:
            if char != ' ':
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = "Hello World This is a Test"
    print(processor.remove_spaces(sample_string))