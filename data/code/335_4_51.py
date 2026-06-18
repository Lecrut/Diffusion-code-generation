import re
class StringSplitter:
    def split(self, text):
        return [word for word in re.split(r'\s+', text.strip()) if word]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "  Hello   world\nthis is a test string. "
    result = splitter.split(sample_text)
    print(result)