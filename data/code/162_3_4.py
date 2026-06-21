class IDGenerator:
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
    generator = IDGenerator()
    gen = generator.generate_ids()
    print(next(gen))
    print(next(gen))
    print(next(gen))