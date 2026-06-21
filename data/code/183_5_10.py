class NameSplitter:
    def split_names(self, line):
        return [name.strip() for name in line.split(',') if name]

if __name__ == '__main__':
    splitter = NameSplitter()
    sample_line = "  Alice, Bob , Charlie,, David  "
    names = splitter.split_names(sample_line)
    print(names)