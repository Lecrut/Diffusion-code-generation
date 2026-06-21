class NameLengthMapper:
    def __init__(self, names):
        self.names = names

    def map_lengths(self):
        return {name: len(name) for name in self.names}

if __name__ == '__main__':
    mapper = NameLengthMapper(['Alice', 'Bob', 'Charlie'])
    print(mapper.map_lengths())