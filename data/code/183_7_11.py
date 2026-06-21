class NameSeparator:
    DELIMITER = ':'

    @staticmethod
    def separate_names(line):
        return [name.strip() for name in line.split(NameSeparator.DELIMITER)]

if __name__ == '__main__':
    sample_line = "  Alice : Bob   : Charlie  "
    result = NameSeparator.separate_names(sample_line)
    print(result)