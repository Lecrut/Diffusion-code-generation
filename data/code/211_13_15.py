import numpy as np

class ArrayComparator:
    def __init__(self, arr1, arr2):
        self.arr1 = np.array(arr1)
        self.arr2 = np.array(arr2)

    def euclidean_distance(self):
        return np.linalg.norm(self.arr1 - self.arr2)

    def cosine_similarity(self):
        dot_product = np.dot(self.arr1, self.arr2)
        norm_arr1 = np.linalg.norm(self.arr1)
        norm_arr2 = np.linalg.norm(self.arr2)
        return dot_product / (norm_arr1 * norm_arr2) if norm_arr1 != 0 and norm_arr2 != 0 else 0

    def correlation_coefficient(self):
        return np.corrcoef(self.arr1, self.arr2)[0, 1]

if __name__ == '__main__':
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    comparator = ArrayComparator(arr1, arr2)
    print("Euclidean Distance:", comparator.euclidean_distance())
    print("Cosine Similarity:", comparator.cosine_similarity())
    print("Correlation Coefficient:", comparator.correlation_coefficient())