class NameListConverter:
    SEPARATOR = '|'

    @staticmethod
    def pipe_to_list(names):
        return [name.strip() for name in names.split(self.SEPARATOR) if name.strip()]

if __name__ == '__main__':
    sample_names = "Alice| Bob |Charlie||David"
    converter = NameListConverter()
    print(converter.pipe_to_list(sample_names))