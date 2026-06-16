class ListComparator:
    def analyze_adjacencies(self, data):
        results = {}
        n = len(data)
        if n < 2:
            return results
        for i in range(n - 1):
            val1 = data[i]
            val2 = data[i+1]
            comparison = None
            if val1 == val2:
                comparison = "equal"
            elif val1 < val2:
                comparison = "less_than"
            else:
                comparison = "greater_than"
            results[f'index_{i}'] = comparison
        return results
if __name__ == '__main__':
    comparator = ListComparator()
    sample_data = [1, 5, 3, 8, 8, 2, 9]
    summary = comparator.analyze_adjacencies(sample_data)
    print(summary)