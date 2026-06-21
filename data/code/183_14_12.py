class NameProcessor:
    def __init__(self, names_str):
        self.names = [name.strip() for name in names_str.split()]

    def get_names(self):
        return self.names

if __name__ == '__main__':
    processor = NameProcessor("  Alice   Bob  Charlie  ")
    print(processor.get_names())