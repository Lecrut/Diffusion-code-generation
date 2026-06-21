class LookupTableBuilder:
    def __init__(self):
        self.lookup_table = {}

    def add_pair(self, key, value):
        self.lookup_table[key] = value

    def get_lookup_table(self):
        return self.lookup_table

if __name__ == '__main__':
    builder = LookupTableBuilder()
    builder.add_pair('apple', 'fruit')
    builder.add_pair('carrot', 'vegetable')
    builder.add_pair('banana', 'fruit')
    builder.add_pair('broccoli', 'vegetable')
    print(builder.get_lookup_table())