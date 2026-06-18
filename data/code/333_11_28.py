class StringProcessor:
    def get_first_chars(self, text):
        result = []
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = [w for w in text.split() if w]
        if not words:
            return ""
        first_chars = set(w[0].lower() for w in words)
        sorted_firsts = "".join(sorted(first_chars))
        return sorted_firsts
if __name__ == '__main__':
    processor = StringProcessor()
    sample_input = "Hello World Python Programming"
    output = processor.get_first_chars(sample_input)
    print(output)