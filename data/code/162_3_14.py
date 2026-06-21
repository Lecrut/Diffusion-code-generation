class IDGenerator:
    def __init__(self):
        self.names = {
            "Alice": 1,
            "Bob": 2,
            "Charlie": 3,
            "David": 4,
            "Eve": 5
        }

    def get_id(self, name):
        return self.names.get(name)

if __name__ == '__main__':
    generator = IDGenerator()
    print(generator.get_id("Alice"))
    print(generator.get_id("Bob"))
    print(generator.get_id("Charlie"))