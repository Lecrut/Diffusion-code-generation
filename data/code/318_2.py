class AdjacentComparator:
    def compare_adjacent(self, data):
        results = []
        for i in range(len(data) - 1):
            a = data[i]
            b = data[i+1]
            comparison_result = 0
            if a < b:
                comparison_result = -1
            elif a > b:
                comparison_result = 1
            else:
                comparison_result = 0
            results.append((a, b, comparison_result))
        return results
if __name__ == '__main__':
    comparator = AdjacentComparator()
    sample_list = [1, 5, 2, 8, 3]
    comparison_results = comparator.compare_adjacent(sample_list)
    print(comparison_results)