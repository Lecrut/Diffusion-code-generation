class NameSeparator:
    def split_names(self, text):
        return [name for name in text.split() if name]

if __name__ == '__main__':
    separator = NameSeparator()
    sample_text = "Alice Bob  Charlie   "
    names = separator.split_names(sample_text)
    print(names)