class StringIndexer:
    def __init__(self, hardcoded_string):
        self.hardcoded_string = hardcoded_string

    def get_char_index_mapping(self):
        return {char: index for index, char in enumerate(self.hardcoded_string)}

if __name__ == '__main__':
    indexer = StringIndexer("hello world")
    print(indexer.get_char_index_mapping())