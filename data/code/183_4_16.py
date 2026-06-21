class NameConverter:
    def __init__(self, names_str):
        self.names_str = names_str

    def convert_to_list(self):
        return [name.strip() for name in self.names_str.split('\n') if name.strip()]

if __name__ == '__main__':
    sample_names = """Alice
Bob
Charlie"""
    converter = NameConverter(sample_names)
    print(converter.convert_to_list())