class ListComparator:
    def compare_adjacent(self, data):
        results = []
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                results.append("decreasing")
            elif data[i] < data[i + 1]:
                results.append("increasing")
            else:
                results.append("equal")
        return results

if __name__ == '__main__':
    comparator = ListComparator()
    sample_data = [1, 5, 2, 8, 8, 3]
    comparison_results = comparator.compare_adjacent(sample_data)
    print(comparison_results)