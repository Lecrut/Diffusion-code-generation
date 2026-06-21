class NameProcessor:
    def __init__(self, names_str):
        self.names_str = names_str

    def process_names(self):
        return [name.strip() for name in self.names_str.split()]

if __name__ == '__main__':
    sample_names = "  John   Doe  Jane Smith  "
    processor = NameProcessor(sample_names)
    processed_names = processor.process_names()
    print(processed_names)