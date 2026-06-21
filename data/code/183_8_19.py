class NameSplitter:
    def split_names(self, input_string: str) -> list[str]:
        names = []
        for part in input_string.split(' and '):
            name_parts = part.strip().split('\n')
            names.extend([name.strip() for name in name_parts if name.strip()])
        return names

if __name__ == '__main__':
    splitter = NameSplitter()
    print(splitter.split_names("Alice\nand Bob\nand Charlie"))
    print(splitter.split_names("\nJohn\nand\nJane\nDoe\nand\nFoo"))