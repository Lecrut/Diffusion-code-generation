class MaxFinder:
    def __init__(self, data):
        self.data = data
        self._max_value = None
        self._setup()
    def _setup(self):
        if not self.data:
            self._max_value = None
            return
        self._max_value = self.data[0]
        for x in self.data[1:]:
            if x > self._max_value:
                self._max_value = x
    def get_maximum(self):
        if self._max_value is None:
            raise ValueError("The list is empty")
        return self._max_value
if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 8, 15]
    mf1 = MaxFinder(sample_data1)
    print(f"Maximum of {sample_data1}: {mf1.get_maximum()}")
    sample_data2 = [-5, -1, -10, -3]
    mf2 = MaxFinder(sample_data2)
    print(f"Maximum of {sample_data2}: {mf2.get_maximum()}")
    sample_data3 = [42]
    mf3 = MaxFinder(sample_data3)
    print(f"Maximum of {sample_data3}: {mf3.get_maximum()}")
    sample_data4 = []
    mf4 = MaxFinder(sample_data4)
    try:
        mf4.get_maximum()
    except ValueError as e:
        print(f"Error for empty list: {e}")