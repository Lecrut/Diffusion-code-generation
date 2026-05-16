class ArrayComparator:
    def check_adjacencies(self, arr):
        result = []
        for i in range(len(arr) - 1):
            comparison = (arr[i], arr[i+1])
            result.append(comparison)
        return result
if __name__ == '__main__':
    comparator = ArrayComparator()
    sample_array = [1, 5, 2, 8, 3]
    comparison_results = comparator.check_adjacencies(sample_array)
    print(comparison_results)