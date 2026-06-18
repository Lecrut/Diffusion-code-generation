class StringSplitter:
    def split(self, text):
        return [word for word in self._split_regex(text) if len(word.strip()) > 0]
    def _split_regex(self, text):
        import re
        parts = re.split(r'\s+', text.strip())
        yield from parts
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "Hello   world\nthis is\t  a test"
    result = splitter.split(sample_text)
    print(result)