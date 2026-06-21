class NameProcessor:
    def __init__(self):
        self.names = []

    def add_names(self, input_string):
        if not input_string:
            return
        names = [name.strip() for name in input_string.split(',')]
        unique_names = set(name for name in names if len(name) > 5)
        self.names.extend(unique_names)

    def get_names(self):
        return sorted(list(self.names))

if __name__ == '__main__':
    processor = NameProcessor()
    sample_input = " Alice , Bob ,  Charlie , alice , Bob "
    processor.add_names(sample_input)
    result = processor.get_names()
    print(result)