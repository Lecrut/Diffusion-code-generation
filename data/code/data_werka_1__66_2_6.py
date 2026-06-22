class ArrayComparator:
    def check_adjacencies(self, numbers):
        return [(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [7, 14, 21, 28, 35]

    print("Comparisons for sample_list_1:")
    comparison_results_1 = comparator.check_adjacencies(sample_list_1)
    print(comparison_results_1)

    print("\nComparisons for sample_list_2:")
    comparison_results_2 = comparator.check_adjacencies(sample_list_2)
    print(comparison_results_2)