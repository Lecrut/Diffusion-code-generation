class NameSeparator:
    def separate_names(self, line):
        return [name.strip() for name in line.split(':')]

if __name__ == '__main__':
    separator = NameSeparator()
    sample_line = "  Alice : Bob   : Charlie  "
    result = separator.separate_names(sample_line)
    print(result)