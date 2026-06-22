class SequenceComparer:
    def analyze_adjacency(self, data):
        results = []
        n = len(data)
        for i in range(n - 1):
            a = data[i]
            b = data[i+1]
            if a > b:
                relationship = 'decreasing'
            elif a < b:
                relationship = 'increasing'
            else:
                relationship = 'equal'
            results.append(relationship)
        return results

if __name__ == '__main__':
    comparer = SequenceComparer()
    sample_data = [10, 5, 5, 20, 15]
    print(comparer.analyze_adjacency(sample_data))