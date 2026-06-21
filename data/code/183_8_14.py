class NameSplitter:

    def split_names(self, names_string):
        return [name.strip() for name in names_string.split('and') if name.strip()]
if __name__ == '__main__':
    splitter = NameSplitter()
    sample_input = 'Alice and Bob and Charlie'
    result = splitter.split_names(sample_input)
    print(result)