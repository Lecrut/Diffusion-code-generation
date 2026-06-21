import numpy as np

class ArrayComparator:
    def __init__(self, array1, array2):
        self.array1 = np.array(array1)
        self.array2 = np.array(array2)

    @staticmethod
    def euclidean_distance(arr1, arr2):
        return np.linalg.norm(arr1 - arr2)

    @staticmethod
    def cosine_similarity(arr1, arr2):
        dot_product = np.dot(arr1, arr2)
        norm_arr1 = np.linalg.norm(arr1)
        norm_arr2 = np.linalg.norm(arr2)
        return dot_product / (norm_arr1 * norm_arr2)

    @staticmethod
    def correlation_coefficient(arr1, arr2):
        return np.corrcoef(arr1, arr2)[0, 1]

if __name__ == '__main__':
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    comparator = ArrayComparator(array1, array2)
    print("Euclidean Distance:", comparator.euclidean_distance(array1, array2))
    print("Cosine Similarity:", comparator.cosine_similarity(array1, array2))
    print("Correlation Coefficient:", comparator.correlation_coefficient(array1, array2))