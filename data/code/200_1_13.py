class StringProcessor:
    def __init__(self, strings):
        self.strings = strings

    def process(self):
        return (s.strip().lower() for s in self.strings)

if __name__ == '__main__':
    sample_values = ["  Hello World  ", "Python Programming", "  Data Science  "]
    processor = StringProcessor(sample_values)
    processed_values = list(processor.process())
    print(processed_values)