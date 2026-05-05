class ArrayComparator:
    def check_adjacencies(self, arr):
        results = []
        for i in range(len(arr) - 1):
            comparison = (arr[i], arr[i+1])
            results.append(comparison)
        return results
if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array = [1, 5, 2, 8, 3]
    comparison_results = comparator.check_adjacencies(sample_array)
    print(comparison_results)