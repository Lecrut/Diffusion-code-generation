class NameProcessor:
    SEPARATOR = '-'

    @staticmethod
    def trim_names(name_string):
        return [name.strip() for name in name_string.split(NameProcessor.SEPARATOR)]

if __name__ == '__main__':
    sample_input = "  John-Doe - Jane-Smith  "
    processor = NameProcessor()
    print(processor.trim_names(sample_input))