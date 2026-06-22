class ArrayComparator:
    def check_adjacencies(self, numbers):
        comparisons = []
        for index in range(len(numbers) - 1):
            pair = (numbers[index], numbers[index + 1])
            comparisons.append(pair)
        return comparisons

if __name__ == '__main__':
    comparator_instance = ArrayComparator()
    sample_numbers = [4, 7, 1, 9, 2]
    adjacency_results = comparator_instance.check_adjacencies(sample_numbers)
    print(adjacency_results)