class StringLengthGrouper:
    @staticmethod
    def group_by_length(strings):
        return {len(s): [s for s in strings if len(s) == k] for k in set(len(s) for s in strings)}

if __name__ == '__main__':
    sample_strings = ["apple", "bee", "cat", "dog", "elephant"]
    result = StringLengthGrouper.group_by_length(sample_strings)
    print(result)