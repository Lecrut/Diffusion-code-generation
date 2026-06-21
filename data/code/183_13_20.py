class NameProcessor:
    def __init__(self, names):
        self.names = names

    def process(self):
        return [name.strip() for name in self.names.split('|') if name.strip()]

if __name__ == '__main__':
    processor = NameProcessor("Alice| Bob |Charlie||David")
    print(processor.process())