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
    print("Data:", sample_data1)
    result1 = comparator.analyze_adjacencies(sample_data1)
    print("Adjacency Analysis 1:", result1)
    sample_data2 = [10, 10, 5, 5, 1]
    print("\nData:", sample_data2)
    result2 = comparator.analyze_adjacencies(sample_data2)
    print("Adjacency Analysis 2:", result2)
    sample_data3 = [4, 4, 4, 4]
    print("\nData:", sample_data3)
    result3 = comparator.analyze_adjacencies(sample_data3)
    print("Adjacency Analysis 3:", result3)