class NameSplitter:
    DELIMITER = ','
    
    @staticmethod
    def split_names(line):
        return [name.strip() for name in line.split(NameSplitter.DELIMITER) if name]

if __name__ == '__main__':
    sample_line = " Alice, Bob , Charlie , David "
    print(NameSplitter.split_names(sample_line))