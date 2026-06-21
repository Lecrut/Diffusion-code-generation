class NameProcessor:
    def __init__(self, name_string):
        self.name_string = name_string

    def trim_names(self):
        return [name.strip() for name in self.name_string.split('-')]

if __name__ == '__main__':
    processor = NameProcessor("  John-Doe - Jane-Smith  ")
    trimmed_names = processor.trim_names()
    print(trimmed_names)