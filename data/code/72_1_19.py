class ElementComparator:
    def __init__(self, list_one, list_two):
        self.list_one = list_one
        self.list_two = list_two

    def compare_at_index(self, index):
        if index < 0 or index >= len(self.list_one) or index >= len(self.list_two):
            raise ValueError("Index out of range for one or both lists")
        val1 = self.list_one[index]
        val2 = self.list_two[index]
        if val1 > val2:
            return (1, val1, val2)
        elif val1 < val2:
            return (-1, val1, val2)
        else:
            return (0, val1, val2)

if __name__ == '__main__':
    comp = ElementComparator([10, 20, 30], [10, 15, 30])
    print(comp.compare_at_index(0))
    print(comp.compare_at_index(1))
    print(comp.compare_at_index(2))