class NameProcessor:
    def __init__(self, names_str):
        self.names = [name.strip() for name in names_str.split(',')]

    def get_stripped_names(self):
        return self.names

if __name__ == '__main__':
    sample_names = "  Alice, Bob , Charlie "
    processor = NameProcessor(sample_names)
    print(processor.get_stripped_names())