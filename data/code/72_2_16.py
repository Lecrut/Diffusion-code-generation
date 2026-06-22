class ListComparator:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def compare_at_index(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(self.list_a) or index >= len(self.list_b):
            raise ValueError("Index out of range for one or both lists")
        
        val_a = self.list_a[index]
        val_b = self.list_b[index]
        
        if val_a < val_b:
            op = '<'
        elif val_a > val_b:
            op = '>'
        else:
            op = '='
            
        return {
            'element1': val_a,
            'element2': val_b,
            'operator': op
        }

if __name__ == '__main__':
    comparator = ListComparator([10, 20, 30], [10, 15, 30])
    result1 = comparator.compare_at_index(0)
    result2 = comparator.compare_at_index(1)
    result3 = comparator.compare_at_index(2)
    print(result1)
    print(result2)
    print(result3)