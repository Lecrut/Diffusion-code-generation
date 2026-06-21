class StringTokenizer:
    def __init__(self, input_str):
        self.segments = self._tokenize(input_str)

    @staticmethod
    def _tokenize(input_str):
        return [segment for segment in input_str.replace('-', ' ').replace('_', ' ').split() if segment.isalnum()]

    def get_segments(self):
        return self.segments

if __name__ == '__main__':
    tokenizer = StringTokenizer("hello-world_example-text")
    print(tokenizer.get_segments())