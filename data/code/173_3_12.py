class StringGrouper:
    def __init__(self, strings):
        self.strings = strings

    def group_by_length(self):
        return {len(s): [s for s in self.strings if len(s) == k] for k in set(len(s) for s in self.strings)}

if __name__ == '__main__':
    grouper = StringGrouper(["apple", "bee", "cat", "dog", "elephant"])
    print(grouper.group_by_length())