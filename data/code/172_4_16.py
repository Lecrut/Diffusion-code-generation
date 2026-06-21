def constant_to_word_mapping():
    return {
        "ONE": "one",
        "TWO": "two",
        "THREE": "three"
    }

class MappingPrinter:
    def __init__(self, mapping):
        self.mapping = mapping

    def print_mapping(self):
        for key, value in self.mapping.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    sample_mapping = constant_to_word_mapping()
    printer = MappingPrinter(sample_mapping)
    printer.print_mapping()