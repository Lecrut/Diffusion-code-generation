import numpy as np

class ArrayProcessor:
    def __init__(self, data):
        self.data = np.array(data)

    def compute_average(self):
        return np.mean(self.data)

if __name__ == '__main__':
    processor = ArrayProcessor([1.0, 2.0, 3.0, 4.0, 5.0])
    print(processor.compute_average())