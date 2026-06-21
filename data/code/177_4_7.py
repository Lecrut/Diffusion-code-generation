class TextSplitter:
    WHITESPACE_CHARS = " \t\n\r\f\v"

    @staticmethod
    def split_text(text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        result = []
        start = 0
        
        for i in range(len(text)):
            if text[i] in TextSplitter.WHITESPACE_CHARS:
                if start < i:
                    result.append(text[start:i])
                start = i + 1
        if start < len(text):
            result.append(text[start:])
        
        return result

if __name__ == '__main__':
    sample_text = "Hello World This is a test"
    splitter = TextSplitter()
    print(splitter.split_text(sample_text))