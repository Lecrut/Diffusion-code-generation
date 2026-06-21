class NameSplitter:
    def split_by_tab(self, text):
        return [name.strip() for name in text.split('\t') if name.strip()]

if __name__ == '__main__':
    splitter = NameSplitter()
    sample_text = "Alice\tBob\nCharlie\tDavid\tEve\nFrank"
    names = splitter.split_by_tab(sample_text)
    print(names)