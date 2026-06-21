import numpy as np

class ArrayAccessor:
    def __init__(self, data):
        self.data = np.asarray(data)

    def get_first(self):
        return self.data.flat[0]

    def get_shape(self):
        return self.data.shape

if __name__ == '__main__':
    large_dataset = np.arange(1000000, dtype=np.int64) + 5
    accessor = ArrayAccessor(large_dataset)
    print(accessor.get_first())
    print(accessor.get_shape())