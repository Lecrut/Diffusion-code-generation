class ElementComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_at_index(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(self.list1) or index >= len(self.list2):
            raise IndexError("Index out of range")
        
        val1 = self.list1[index]
        val2 = self.list2[index]
        
        if val1 > val2:
            return 1
        elif val1 < val2:
            return -1
        else:
            return 0

if __name__ == '__main__':
    l1 = [10, 25, 30]
    l2 = [10, 20, 35]
    comp = ElementComparator(l1, l2)
    
    idx0 = comp.compare_at_index(0)
    idx1 = comp.compare_at_index(1)
    idx2 = comp.compare_at_index(2)
    
    print(f"Index 0: {idx0}")
    print(f"Index 1: {idx1}")
    print(f"Index 2: {idx2}")