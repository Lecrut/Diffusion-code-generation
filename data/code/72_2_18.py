class ListComparator:
    _RESULT_MAP = {
        -1: '<',
        0: '=',
        1: '>'
    }

    def compare_at_index(self, list_a, list_b, idx):
        if not isinstance(idx, int):
            raise ValueError("Index must be an integer")
        if idx < 0 or idx >= len(list_a) or idx >= len(list_b):
            raise ValueError("Index out of bounds")
        
        val_a = list_a[idx]
        val_b = list_b[idx]
        
        if val_a < val_b:
            diff = -1
        elif val_a > val_b:
            diff = 1
        else:
            diff = 0
            
        return {
            'left': val_a,
            'right': val_b,
            'op': self._RESULT_MAP[diff]
        }

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([10, 20, 30], [5, 25, 30], 1)
    print(result)