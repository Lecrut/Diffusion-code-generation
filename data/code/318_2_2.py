class AdjacentComparator:
    def compare_adjacent(self, data):
        results = []
        for i in range(len(data) - 1):
            result = (data[i], data[i+1])
            results.append(result)
        return results
if __name__ == '__main__':
    comparator = AdjacentComparator()
    sample_list = [1, 5, 2, 8, 3]
    comparison_results = comparator.compare_adjacent(sample_list)
    print(comparison_results)