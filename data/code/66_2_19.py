class ArrayComparator:
    ADJACENCY_PAIR = (0, 1)

    def check_adjacencies(self, numbers):
        result = []
        for i in range(len(numbers) - 1):
            comparison = (numbers[i], numbers[i + self.ADJACENCY_PAIR[1]])
            result.append(comparison)
        return result

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_list = [4, 9, 2, 6, 5]
    comparison_results = comparator.check_adjacencies(sample_list)
    print(comparison_results)