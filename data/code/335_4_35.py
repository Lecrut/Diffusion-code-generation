import re
class StringSplitter:
    def split(self, text):
        return [word for word in re.split(r'\s+', text.strip()) if len(word) > 0]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "   hello world\nthis is a test string\twith irregular spaces"
    result = splitter.split(sample_text)
    print(result)