class ArrayComparator:
    ADJACENCY_PAIR_FORMAT = '({}, {})'

    def check_adjacencies(self, numbers):
        result = []
        for i in range(len(numbers) - 1):
            comparison = self.ADJACENCY_PAIR_FORMAT.format(numbers[i], numbers[i+1])
            result.append(comparison)
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_values = [4, 9, 2, 6, 5]
    comparison_results = comparator.check_adjacencies(sample_values)
    print(comparison_results)