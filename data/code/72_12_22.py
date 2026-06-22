class AdjacentComparator:
    DIFFERENCE_MARKER = "!="

    def __init__(self, data):
        self.data = data

    def find_inequalities(self):
        results = []
        length = len(self.data)
        if length < 2:
            return results
        for i in range(length - 1):
            current = self.data[i]
            next_val = self.data[i + 1]
            if current != next_val:
                results.append((i, current, next_val))
        return results

if __name__ == '__main__':
    sample_values = [10, 10, 20, 30, 30, 40, 50]
    comparator = AdjacentComparator(sample_values)
    output = comparator.find_inequalities()
    print(output)