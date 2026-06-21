class IdGenerator:
    def __init__(self):
        self.names = {
            "Alice": 1,
            "Bob": 2,
            "Charlie": 3,
            "David": 4,
            "Eve": 5
        }

    def generate_ids(self):
        for name, id in self.names.items():
            yield (name, id)

if __name__ == '__main__':
    gen = IdGenerator()
    print(next(gen.generate_ids()))
    print(next(gen.generate_ids()))
    print(next(gen.generate_ids()))