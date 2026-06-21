class TextSplitter:
    SEPARATORS = " \t\n\r\f\v"

    @staticmethod
    def split_text(text):
        result = []
        word_buffer = []
        for char in text:
            if char in TextSplitter.SEPARATORS:
                if word_buffer:
                    result.append(''.join(word_buffer))
                    word_buffer.clear()
            else:
                word_buffer.append(char)
        if word_buffer:
            result.append(''.join(word_buffer))
        return result

if __name__ == '__main__':
    sample_text = "Hello World This is a test"
    splitter = TextSplitter()
    result = splitter.split_text(sample_text)
    print(result)