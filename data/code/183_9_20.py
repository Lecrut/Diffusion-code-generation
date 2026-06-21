class NameProcessor:
    @staticmethod
    def trim_names(name_string):
        return [name.strip() for name in name_string.split('-')]

if __name__ == '__main__':
    processor = NameProcessor()
    sample_input = "  John-Doe - Jane-Smith  "
    trimmed_names = processor.trim_names(sample_input)
    print(trimmed_names)