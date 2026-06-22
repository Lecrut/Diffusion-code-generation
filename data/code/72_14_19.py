class ArrayComparator:
    MATCH_LABEL = 'match'
    MISMATCH_LABEL = 'mismatch'

    def __init__(self, array_a, array_b):
        self.array_a = array_a
        self.array_b = array_b

    @staticmethod
    def _validate_indices(indices, length_a, length_b):
        valid_indices = []
        for idx in indices:
            if 0 <= idx < length_a and 0 <= idx < length_b:
                valid_indices.append(idx)
        return valid_indices

    def count_matches_at_positions(self, indices):
        count = 0
        valid_indices = self._validate_indices(indices, len(self.array_a), len(self.array_b))
        for idx in valid_indices:
            if self.array_a[idx] == self.array_b[idx]:
                count += 1
        return count

if __name__ == '__main__':
    data_first = [5, 10, 15, 20, 25]
    data_second = [5, 12, 15, 22, 25]
    target_positions = [0, 2, 4]
    comparator = ArrayComparator(data_first, data_second)
    matches = comparator.count_matches_at_positions(target_positions)
    print(matches)