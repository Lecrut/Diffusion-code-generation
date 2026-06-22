class IndexPairComparer:
    def __init__(self, data):
        self.data = list(data)
        self.size = len(self.data)

    def _check_bounds(self, index):
        if index < 0 or index >= self.size:
            raise ValueError(f"Index {index} is out of bounds for data of length {self.size}")

    def compare_pairs(self, indices):
        if not indices:
            return []
        results = []
        for i in range(len(indices) - 1):
            idx_a = indices[i]
            idx_b = indices[i + 1]
            self._check_bounds(idx_a)
            self._check_bounds(idx_b)
            val_a = self.data[idx_a]
            val_b = self.data[idx_b]
            if val_a < val_b:
                results.append(f"{val_a} < {val_b}")
            elif val_a > val_b:
                results.append(f"{val_a} > {val_b}")
            else:
                results.append(f"{val_a} == {val_b}")
        return results

    def compare_adjacent(self, start_index):
        self._check_bounds(start_index)
        if start_index + 1 >= self.size:
            raise ValueError(f"Cannot compare adjacent elements starting at {start_index} in data of length {self.size}")
        val_a = self.data[start_index]
        val_b = self.data[start_index + 1]
        if val_a < val_b:
            return f"{val_a} < {val_b}"
        elif val_a > val_b:
            return f"{val_a} > {val_b}"
        else:
            return f"{val_a} == {val_b}"

if __name__ == '__main__':
    sample_data = [10, 20, 15, 30, 25]
    comparer = IndexPairComparer(sample_data)
    print(comparer.compare_pairs([0, 2, 4]))
    print(comparer.compare_adjacent(1))
    print(comparer.compare_adjacent(3))