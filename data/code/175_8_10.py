class StringTokenizer:
    DELIMITERS = '-_'

    @staticmethod
    def tokenize(input_str):
        cleaned_str = ''.join([char if char.isalnum() else ' ' for char in input_str])
        return [segment for segment in cleaned_str.split() if segment]

if __name__ == '__main__':
    sample = "hello-world_example-text"
    tokenizer = StringTokenizer()
    print(tokenizer.tokenize(sample))