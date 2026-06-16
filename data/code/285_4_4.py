class SequenceComparer:
    def analyze_adjacency(self, data):
        results = {}
        n = len(data)
        if n < 2:
            return results
        for i in range(n - 1):
            a = data[i]
            b = data[i+1]
            if a > b:
                relationship = '>'
            elif a < b:
                relationship = '<'
            else:
                relationship = '='
            pair = (i, i + 1)
            results[pair] = relationship
        return results
if __name__ == '__main__':
    comparer = SequenceComparer()
    sample_data = [10, 5, 5, 20, 30, 30, 15]
    analysis = comparer.analyze_adjacency(sample_data)
    print(analysis)