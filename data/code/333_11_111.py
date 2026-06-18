class StringProcessor:
    def first_chars(self, text):
        result = []
        prev_space = -1
        for i in range(len(text)):
            if text[i] == ' ':
                prev_space = i
            elif not (i > 0 and text[i-1].isspace()) or prev_space != -1:
                continue
            else:
                result.append(text[prev_space + 1:i])
        return ''.join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_string = "Hello World Python Programming"
    output = processor.first_chars(test_string)
    print(output)