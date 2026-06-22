class StringAccumulator:
    def __init__(self):
        self.content = ""

    def add(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        self.content += text

    def get_content(self):
        return self.content

if __name__ == '__main__':
    accumulator = StringAccumulator()
    accumulator.add("Hello")
    accumulator.add(" ")
    accumulator.add("World")
    print(accumulator.get_content())