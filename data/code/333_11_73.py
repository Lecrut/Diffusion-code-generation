class StringProcessor:
    def get_first_chars(self, text: str) -> str:
        return ''.join(word[0] for word in text.split() if word)
if __name__ == '__main__':
    sp = StringProcessor()
    sample_input = "Hello world Python programming is fun today"
    result = sp.get_first_chars(sample_input)
    print(result)