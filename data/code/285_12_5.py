class ListComparator:
    def analyze_adjacencies(self, data):
        results = {}
        n = len(data)
        for i in range(n - 1):
            item1 = data[i]
            item2 = data[i+1]
            comparison_result = None
            if item1 == item2:
                comparison_result = "equal"
            elif item1 < item2:
                comparison_result = "less_than"
            else:
                comparison_result = "greater_than"
            results[str(i)] = comparison_result
        return results
if __name__ == '__main__':
    comparator = ListComparator()
    sample_data1 = [1, 5, 2, 8, 3]
    print("Sample Data 1:")
    print(comparator.analyze_adjacencies(sample_data1))
    sample_data2 = [10, 10, 5, 5, 1]
    print("\nSample Data 2:")
    print(comparator.analyze_adjacencies(sample_data2))
    sample_data3 = [42, 42, 42, 42]
    print("\nSample Data 3:")
    print(comparator.analyze_adjacencies(sample_data3))
    sample_data4 = [1, 2, 3, 4, 5]
    print("\nSample Data 4:")
    print(comparator.analyze_adjacencies(sample_data4))