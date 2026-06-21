class StringGroup:
    def __init__(self, strings):
        self.strings = strings

    def group_by_length(self):
        return {len(s): [s for s in self.strings if len(s) == k] for k in set(len(s) for s in self.strings)}

if __name__ == '__main__':
    sample_strings = ["apple", "bee", "cat", "dog", "elephant"]
    string_group = StringGroup(sample_strings)
    grouped_by_length = string_group.group_by_length()
    print(grouped_by_length)