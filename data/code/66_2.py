class ArrayComparator:
    def check_adjacencies(self, numbers):
        result = []
        for i in range(len(numbers) - 1):
            comparison = (numbers[i], numbers[i+1])
            result.append(comparison)
        return result
if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_list = [1, 5, 2, 8, 3]
    comparison_results = comparator.check_adjacencies(sample_list)
    print(comparison_results)