class OptimizedList:
    def __init__(self, initial_list):
        self._data = list(initial_list)
        self._set = set(self._data)
    def contains(self, element):
        return element in self._set
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3, 5]
    opt_list = OptimizedList(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Checking for 2: {opt_list.contains(2)}")
    print(f"Checking for 5: {opt_list.contains(5)}")
    print(f"Checking for 9: {opt_list.contains(9)}")
    print(f"Checking for 1: {opt_list.contains(1)}")
    print(f"Checking for 8: {opt_list.contains(8)}")