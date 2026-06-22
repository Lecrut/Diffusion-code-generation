class PairComparator:
    def __init__(self, data):
        self.data = list(data)
        self.length = len(self.data)

    def compare(self, indices):
        if not indices:
            return []
        results = []
        for i in range(len(indices) - 1):
            idx1 = indices[i]
            idx2 = indices[i + 1]
            self._validate_index(idx1)
            self._validate_index(idx2)
            val1 = self.data[idx1]
            val2 = self.data[idx2]
            if val1 < val2:
                results.append(f"{val1} < {val2}")
            elif val1 > val2:
                results.append(f"{val1} > {val2}")
            else:
                results.append(f"{val1} == {val2}")
        return results

    def _validate_index(self, idx):
        if not isinstance(idx, int):
            raise TypeError(f"Index must be an integer, got {type(idx).__name__}")
        if idx < 0 or idx >= self.length:
            raise ValueError(f"Index {idx} is out of range for data of length {self.length}")

if __name__ == '__main__':
    sample_data = [10, 20, 15, 30, 25]
    sample_indices = [0, 2, 4]
    comparator = PairComparator(sample_data)
    output = comparator.compare(sample_indices)
    print(output)