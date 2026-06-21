class NameProcessor:
    def __init__(self):
        self.names = []

    def add_names(self, names):
        self.names.extend(names)

    def process_names(self):
        return sorted(set(name.upper() for name in self.names), reverse=True)

if __name__ == '__main__':
    processor = NameProcessor()
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    processor.add_names(sample_names)
    print(processor.process_names())