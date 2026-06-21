class StringSplitter:
    def __init__(self):
        self.sample_string = "split this string by spaces"

    def split(self):
        return self.sample_string.split()

if __name__ == '__main__':
    splitter = StringSplitter()
    result = splitter.split()
    print(result)