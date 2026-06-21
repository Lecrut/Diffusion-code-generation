class IndexComparator:
    def __init__(self, primary_list, secondary_list):
        self.primary = primary_list
        self.secondary = secondary_list

    def check_order(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0:
            raise ValueError("Index cannot be negative")
        if index >= len(self.primary):
            raise ValueError("Index out of bounds for primary list")
        if index >= len(self.secondary):
            raise ValueError("Index out of bounds for secondary list")
        return self.primary[index] <= self.secondary[index]

    def get_elements(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0:
            raise ValueError("Index cannot be negative")
        if index >= len(self.primary):
            raise ValueError("Index out of bounds for primary list")
        if index >= len(self.secondary):
            raise ValueError("Index out of bounds for secondary list")
        return self.primary[index], self.secondary[index]

if __name__ == '__main__':
    list_one = [5, 10, 15]
    list_two = [5, 20, 10]
    comp = IndexComparator(list_one, list_two)
    print(comp.check_order(0))
    print(comp.check_order(1))
    print(comp.check_order(2))
    print(comp.get_elements(0))
    print(comp.get_elements(2))