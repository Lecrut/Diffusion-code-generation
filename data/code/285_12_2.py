class ListComparator:
    def analyze_adjacencies(self, data):
        results = {}
        n = len(data)
        for i in range(n - 1):
            item1 = data[i]
            item2 = data[i+1]
            comparison_result = None
            if item1 > item2:
                comparison_result = "greater"
            elif item1 < item2:
                comparison_result = "less"
            else:
                comparison_result = "equal"
            results[f'index_{i}'] = comparison_result
        return results
if __name__ == '__main__':
    comparator = ListComparator()
    sample_data = [10, 5, 20, 20, 3, 15]
    summary = comparator.analyze_adjacencies(sample_data)
    print(summary)