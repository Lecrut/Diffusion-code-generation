class NameProcessor:
    def __init__(self, names):
        self.names = names

    def process_names(self):
        return [name.strip() for name in self.names.split('|') if name.strip()]

if __name__ == '__main__':
    sample_names = "Alice| Bob |Charlie||David"
    processor = NameProcessor(sample_names)
    print(processor.process_names())