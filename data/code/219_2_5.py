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
    sample_data1 = [10, 5, 20, 8, 15]
    mf.add_data(sample_data1)
    print(mf.get_maximum())
    mf2 = MaxFinder()
    sample_data2 = [-5, -1, -10, -3]
    mf2.add_data(sample_data2)
    print(mf2.get_maximum())
    mf3 = MaxFinder()
    empty_data = []
    mf3.add_data(empty_data)
    try:
        mf3.get_maximum()
    except ValueError as e:
        print(e)