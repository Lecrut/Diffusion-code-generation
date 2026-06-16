class SequenceComparer:
    def analyze_adjacency(self, data):
        results = {}
        n = len(data)
        for i in range(n - 1):
            a = data[i]
            b = data[i+1]
            if a > b:
                relationship = '>'
            elif a < b:
                relationship = '<'
            else:
                relationship = '='
            results[(i, i + 1)] = relationship
        return results
if __name__ == '__main__':
    comparer = SequenceComparer()
    sample_data = [10, 5, 5, 20, 30]
    analysis = comparer.analyze_adjacency(sample_data)
    print(analysis)