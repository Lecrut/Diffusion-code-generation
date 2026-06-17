import re
class StringSplitter:
    def split(self, text):
        return [word for word in re.split(r'\s+', text) if word]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "  hello world\nthis is a test string   \n"
    result = splitter.split(sample_text)
    print(result)