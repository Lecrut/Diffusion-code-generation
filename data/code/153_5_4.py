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
    print(f"Is 5 present? {opt_list.contains(5)}")
    print(f"Is 10 present? {opt_list.contains(10)}")
    print(f"Is 2 present? {opt_list.contains(2)}")
    print(f"Is 9 present? {opt_list.contains(9)}")