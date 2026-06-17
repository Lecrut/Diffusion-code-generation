class LargestElementFinder:
    def __init__(self):
        self._data = []
        self._largest = None
    def add(self, item):
        self._data.append(item)
        if self._largest is None or item > self._largest:
            self._largest = item
    def get_largest(self):
        return self._largest
if __name__ == '__main__':
    finder = LargestElementFinder()
    sample_data1 = [10, 5, 20, 8, 15]
    for item in sample_data1:
        finder.add(item)
    print(f"Largest element for {sample_data1}: {finder.get_largest()}")
    finder2 = LargestElementFinder()
    sample_data2 = [3, 7, 1, 9, 4]
    for item in sample_data2:
        finder2.add(item)
    print(f"Largest element for {sample_data2}: {finder2.get_largest()}")
    finder3 = LargestElementFinder()
    sample_data3 = [50, 10, 40, 20]
    for item in sample_data3:
        finder3.add(item)
    print(f"Largest element for {sample_data3}: {finder3.get_largest()}")