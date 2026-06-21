class StringTokenizer:
    DELIMITERS = ('-', '_')

    @staticmethod
    def tokenize(input_str):
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")
        
        for delimiter in StringTokenizer.DELIMITERS:
            input_str = input_str.replace(delimiter, ' ')
        
        segments = input_str.split()
        return [segment for segment in segments if segment.isalnum()]

if __name__ == '__main__':
    sample = "hello-world_example-text"
    tokenizer = StringTokenizer()
    print(tokenizer.tokenize(sample))