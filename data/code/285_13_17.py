class StringComparator:
    @staticmethod
    def compare_adjacent(strings):
        return [max(pair) for pair in zip(strings, strings[1:])]

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    comparator = StringComparator()
    result = comparator.compare_adjacent(sample_values)
    print(result)