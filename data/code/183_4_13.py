class NameConverter:
    def __init__(self, names_str):
        self.names = [name.strip() for name in names_str.split('\n') if name.strip()]

    def get_names(self):
        return self.names

if __name__ == '__main__':
    sample_names = """Alice
Bob
Charlie"""
    converter = NameConverter(sample_names)
    print(converter.get_names())