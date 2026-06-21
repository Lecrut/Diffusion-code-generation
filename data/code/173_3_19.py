class StringGrouper:
    def __init__(self, strings):
        self.strings = strings

    def group_by_length(self):
        return {len(s): [s for s in self.strings if len(s) == l] for l in set(len(s) for s in self.strings)}

if __name__ == '__main__':
    sample_strings = ["apple", "bee", "cat", "dog", "elephant"]
    grouper = StringGrouper(sample_strings)
    print(grouper.group_by_length())