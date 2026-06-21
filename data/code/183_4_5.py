class NameConverter:
    def __init__(self, names_str):
        self.names = [name.strip() for name in names_str.split('\n') if name.strip()]

    def get_names_list(self):
        return self.names

if __name__ == '__main__':
    sample_names = "Alice\nBob\nCharlie"
    converter = NameConverter(sample_names)
    print(converter.get_names_list())