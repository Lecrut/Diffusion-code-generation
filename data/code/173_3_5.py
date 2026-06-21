class StringGrouper:
    @staticmethod
    def group_by_length(strings):
        return {len(s): [s for s in strings if len(s) == l] for l in set(len(s) for s in strings)}

if __name__ == '__main__':
    sample_strings = ["apple", "bee", "cat", "dog", "elephant"]
    grouped_by_length = StringGrouper.group_by_length(sample_strings)
    print(grouped_by_length)