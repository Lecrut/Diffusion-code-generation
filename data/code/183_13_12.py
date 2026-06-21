class NameProcessor:
    SEPARATOR = '|'

    @staticmethod
    def pipe_to_list(names):
        return [name.strip() for name in names.split(self.SEPARATOR) if name.strip()]

if __name__ == '__main__':
    sample_names = "Alice| Bob |Charlie||David"
    processor = NameProcessor()
    print(processor.pipe_to_list(sample_names))