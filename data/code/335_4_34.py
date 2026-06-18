import re
class StringSplitter:
    def split(self, text):
        return [word for word in re.findall(r'\S+', text)]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_text = "  Hello   world\nPython\tis great!"
    result = splitter.split(sample_text)
    print(result)