class StringSplitter:
    def __init__(self):
        pass
    def split(self, s: str) -> list[str]:
        return [word for word in s.split() if len(word)]
if __name__ == '__main__':
    splitter = StringSplitter()
    sample_input = "  hello   world\t\nhow are you"
    result_list = splitter.split(sample_input)