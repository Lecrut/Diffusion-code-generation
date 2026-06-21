import numpy as np

class ArrayComparer:
    def __init__(self, arr1, arr2):
        self.arr1 = np.array(arr1)
        self.arr2 = np.array(arr2)

    def calculate_distance(self, distance_type='euclidean'):
        if distance_type == 'euclidean':
            return np.linalg.norm(self.arr1 - self.arr2)
        elif distance_type == 'cosine':
            dot_product = np.dot(self.arr1, self.arr2)
            norm_arr1 = np.linalg.norm(self.arr1)
            norm_arr2 = np.linalg.norm(self.arr2)
            return dot_product / (norm_arr1 * norm_arr2)
        else:
            raise ValueError("Unsupported distance type")

    def correlation_coefficient(self):
        return np.corrcoef(self.arr1, self.arr2)[0, 1]

if __name__ == '__main__':
    array_comparer = ArrayComparer([1, 2, 3], [4, 5, 6])
    print("Euclidean Distance:", array_comparer.calculate_distance('euclidean'))
    print("Cosine Similarity:", array_comparer.calculate_distance('cosine'))
    print("Correlation Coefficient:", array_comparer.correlation_coefficient())