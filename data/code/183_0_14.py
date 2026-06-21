class NameProcessor:
    def __init__(self, names_str):
        self.names_list = names_str.split(',')

    def strip_names(self):
        return [name.strip() for name in self.names_list]

if __name__ == '__main__':
    sample_names = "  Alice, Bob , Charlie "
    processor = NameProcessor(sample_names)
    print(processor.strip_names())