import re
class StringSplitter:
    def split_whitespace(self, text):
        return [word for word in re.split(r'\s+', text) if word]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "  Hello   world\nthis is a test\tstring"
    result = splitter.split_whitespace(sample_text)
    print(result)