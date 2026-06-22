class ElementComparator:
    def __init__(self, dataset):
        self.dataset = tuple(dataset)
        self.size = len(self.dataset)

    def _check_bounds(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= self.size:
            raise ValueError(f"Index {index} is out of range [0, {self.size - 1}]")

    def compare_at(self, idx_a, idx_b):
        self._check_bounds(idx_a)
        self._check_bounds(idx_b)
        val_a = self.dataset[idx_a]
        val_b = self.dataset[idx_b]
        if val_a < val_b:
            return f"{val_a} < {val_b}"
        elif val_a > val_b:
            return f"{val_a} > {val_b}"
        else:
            return f"{val_a} == {val_b}"

    def compare_adjacent_pairs(self, start_index):
        results = []
        idx_a = start_index
        idx_b = start_index + 1
        self._check_bounds(idx_a)
        self._check_bounds(idx_b)
        val_a = self.dataset[idx_a]
        val_b = self.dataset[idx_b]
        if val_a < val_b:
            results.append(f"{val_a} < {val_b}")
        elif val_a > val_b:
            results.append(f"{val_a} > {val_b}")
        else:
            results.append(f"{val_a} == {val_b}")
        return results

if __name__ == '__main__':
    data_list = [42, 15, 98, 12, 67, 30]
    comparator = ElementComparator(data_list)
    result_one = comparator.compare_at(0, 1)
    result_two = comparator.compare_adjacent_pairs(2)
    print(result_one)
    print(result_two)