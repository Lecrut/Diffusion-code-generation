class IndexPairComparator:
    def __init__(self, source_data):
        self._values = list(source_data)
        self._count = len(self._values)

    def _check_bounds(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= self._count:
            raise ValueError(f"Index {index} is out of range for data of size {self._count}")

    def _format_result(self, left_val, right_val):
        if left_val < right_val:
            return f"{left_val} < {right_val}"
        if left_val > right_val:
            return f"{left_val} > {right_val}"
        return f"{left_val} == {right_val}"

    def compare_pairs(self, start_indices):
        results = []
        limit = len(start_indices) - 1
        if limit < 0:
            return results
        
        for k in range(limit):
            current_idx = start_indices[k]
            next_idx = start_indices[k + 1]
            
            self._check_bounds(current_idx)
            self._check_bounds(next_idx)
            
            val_left = self._values[current_idx]
            val_right = self._values[next_idx]
            
            results.append(self._format_result(val_left, val_right))
        
        return results

    def compare_adjacent(self, base_index):
        self._check_bounds(base_index)
        next_index = base_index + 1
        
        if next_index >= self._count:
            raise ValueError(f"Index {base_index} has no adjacent successor in data of size {self._count}")
            
        val_left = self._values[base_index]
        val_right = self._values[next_index]
        
        return self._format_result(val_left, val_right)

if __name__ == '__main__':
    dataset = [100, 200, 150, 300, 250, 400]
    comparator = IndexPairComparator(dataset)
    
    pair_indices = [0, 2, 4]
    pair_results = comparator.compare_pairs(pair_indices)
    for item in pair_results:
        print(item)
        
    single_adjacent_result = comparator.compare_adjacent(1)
    print(single_adjacent_result)