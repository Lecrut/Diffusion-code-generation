def _validate_index(index, length):
    if not isinstance(index, int):
        raise ValueError(f"Index must be integer, got {type(index).__name__}")
    if index < -length or index >= length:
        raise ValueError(f"Index {index} out of bounds for length {length}")
    return index if index >= 0 else length + index

def compare_pairs(data, indices):
    if not isinstance(data, (list, tuple)):
        raise ValueError("Data must be a list or tuple")
    if not isinstance(indices, (list, tuple)):
        raise ValueError("Indices must be a list or tuple")
    if len(indices) < 2:
        raise ValueError("Indices must contain at least two elements")
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    
    validated_indices = [_validate_index(i, len(data)) for i in indices]
    results = []
    for i in range(0, len(validated_indices) - 1, 2):
        idx1 = validated_indices[i]
        idx2 = validated_indices[i + 1]
        val1 = data[idx1]
        val2 = data[idx2]
        if val1 < val2:
            results.append(f"{val1} < {val2}")
        elif val1 > val2:
            results.append(f"{val1} > {val2}")
        else:
            results.append(f"{val1} == {val2}")
    return results

class IndexComparer:
    def __init__(self, data):
        self.data = list(data)
    def compare(self, indices):
        return compare_pairs(self.data, indices)

if __name__ == '__main__':
    sample_data = [42, 10, 99, 5, 50]
    sample_indices = [0, 1, 2, 3]
    comparer = IndexComparer(sample_data)
    result = comparer.compare(sample_indices)
    print(result)