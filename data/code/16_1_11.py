import numpy as np

class ArrayAccessor:
    def __init__(self, data):
        self.data = np.asarray(data)
        if self.data.size == 0:
            raise ValueError("Input array must not be empty")

    def get_initial_value(self):
        return self.data.flat[0]

if __name__ == '__main__':
    test_data = np.array([[5, 12, 8], [3, 9, 1]])
    accessor = ArrayAccessor(test_data)
    print(accessor.get_initial_value())
    
    test_scalar = np.array(7)
    scalar_accessor = ArrayAccessor(test_scalar)
    print(scalar_accessor.get_initial_value())