class ListComparator:
    _OP_MAP = {
        -1: '<',
        0: '=',
        1: '>'
    }

    def compare_at_index(self, list1, list2, index):
        if not isinstance(index, int) or isinstance(index, bool):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise ValueError("Index out of range")
        
        val1 = list1[index]
        val2 = list2[index]
        
        if val1 < val2:
            cmp_val = -1
        elif val1 > val2:
            cmp_val = 1
        else:
            cmp_val = 0
            
        return {
            'left': val1,
            'right': val2,
            'relation': self._OP_MAP[cmp_val]
        }

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([10, 20, 30], [10, 15, 30], 1)
    print(result)