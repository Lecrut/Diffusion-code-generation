class ArrayComparator:
    def check_adjacencies(self, numbers):
        return [(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_data = [4, 9, 1, 6, 3]
    comparison_results = comparator.check_adjacencies(sample_data)
    print(comparison_results)