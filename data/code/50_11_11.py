import numpy as np

class RasterAreaCalculator:

    def __init__(self, matrix1, matrix2):
        self.matrix1 = np.array(matrix1)
        self.matrix2 = np.array(matrix2)

    def calculate_area_difference(self):
        difference_matrix = np.bitwise_xor(self.matrix1, self.matrix2)
        return np.sum(difference_matrix)
if __name__ == '__main__':
    sample_matrix1 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    sample_matrix2 = [[1, 1, 0], [0, 0, 1], [1, 1, 0]]
    calculator = RasterAreaCalculator(sample_matrix1, sample_matrix2)
    difference = calculator.calculate_area_difference()
    print(difference)
    sample_matrix3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    sample_matrix4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    calculator2 = RasterAreaCalculator(sample_matrix3, sample_matrix4)
    difference2 = calculator2.calculate_area_difference()
    print(difference2)
    sample_matrix5 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    sample_matrix6 = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    calculator3 = RasterAreaCalculator(sample_matrix5, sample_matrix6)
    difference3 = calculator3.calculate_area_difference()
    print(difference3)