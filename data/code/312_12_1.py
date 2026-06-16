class LargestElementFinder:
    def __init__(self, data):
        self._data = list(data)
        self._largest = self._find_initial_largest()
    def _find_initial_largest(self):
        if not self._data:
            return None
        largest = self._data[0]
        for x in self._data[1:]:
            if x > largest:
                largest = x
        return largest
    def update(self, new_data):
        if not new_data:
            return
        if len(new_data) > len(self._data):
            self._data = list(new_data)
            self._largest = self._find_initial_largest()
        else:
            for x in new_data:
                if x > self._largest:
                    self._largest = x
    def get_largest(self):
        return self._largest
if __name__ == '__main__':
    sample1 = [10, 5, 20, 8]
    finder1 = LargestElementFinder(sample1)
    print(f"Sample 1 Initial Largest: {finder1.get_largest()}")
    finder1.update([3, 15, 7])
    print(f"Sample 1 After Update: {finder1.get_largest()}")
    sample2 = [42]
    finder2 = LargestElementFinder(sample2)
    print(f"Sample 2 Initial Largest: {finder2.get_largest()}")
    finder2.update([10, 5])
    print(f"Sample 2 After Update: {finder2.get_largest()}")
    sample3 = [99, 1, 50]
    finder3 = LargestElementFinder(sample3)
    print(f"Sample 3 Initial Largest: {finder3.get_largest()}")
    finder3.update([5, 100])
    print(f"Sample 3 After Update: {finder3.get_largest()}")
    sample4 = []
    finder4 = LargestElementFinder(sample4)
    print(f"Sample 4 Initial Largest: {finder4.get_largest()}")
    finder4.update([1, 2])
    print(f"Sample 4 After Update: {finder4.get_largest()}")