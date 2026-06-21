class NameProcessor:
    def __init__(self, name_string):
        self.name_string = name_string.strip()

    def split_names(self):
        return [name.strip() for name in self.name_string.split('-')]

if __name__ == '__main__':
    sample_input = "  John-Doe - Jane-Smith  "
    processor = NameProcessor(sample_input)
    trimmed_names = processor.split_names()
    print(trimmed_names)