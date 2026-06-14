class MaxFinder:
    def __init__(self):
        self._data = []
    def add_data(self, data):
        self._data.extend(data)
    def get_maximum(self):
        if not self._data:
            raise ValueError("The list is empty")
        return max(self._data)
if __name__ == '__main__':
    mf = MaxFinder()
    sample_data1 = [10, 5, 20, 8]
    sample_data2 = [3, 1, 9, 4]
    mf.add_data(sample_data1)
    print(f"Maximum of {sample_data1}: {mf.get_maximum()}")
    mf.add_data(sample_data2)
    print(f"Maximum of {sample_data2}: {mf.get_maximum()}")
    mf.add_data([100, 50, 75])
    print(f"Maximum of the combined set: {mf.get_maximum()}")