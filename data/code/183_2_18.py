class NameSeparator:
    def split_names(self, names):
        return [name for name in names.split() if name]

if __name__ == '__main__':
    separator = NameSeparator()
    sample_names = "Alice Bob  Charlie   "
    result = separator.split_names(sample_names)
    print(result)