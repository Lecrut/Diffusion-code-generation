class NameProcessor:
    def __init__(self, names):
        self.names = names

    def process_names(self):
        return sorted(set(name.upper() for name in self.names), reverse=True)

if __name__ == '__main__':
    processor = NameProcessor(['Alice', 'bob', 'Charlie', 'alice', 'Bob'])
    print(processor.process_names())