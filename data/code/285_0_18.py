class DataComparator:
    def compare_adjacent(self, data):
        results = []
        for i in range(len(data) - 1):
            a = data[i]
            b = data[i+1]
            if a > b:
                results.append("decreasing")
            elif a < b:
                results.append("increasing")
            else:
                results.append("equal")
        return results

if __name__ == '__main__':
    comparator = DataComparator()
    sample_data = [1, 5, 2, 8, 8, 3]
    comparison_results = comparator.compare_adjacent(sample_data)
    print(comparison_results)