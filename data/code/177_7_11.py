class StringSplitter:
    def __init__(self, input_string):
        self.input_string = input_string

    def split(self):
        return self.input_string.split()

if __name__ == '__main__':
    splitter = StringSplitter('Python is awesome')
    words = splitter.split()
    print(words)