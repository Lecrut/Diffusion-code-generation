import numpy as np

class ArrayComparer:
    def euclidean_distance(self, arr1, arr2):
        return np.linalg.norm(arr1 - arr2)

    def cosine_similarity(self, arr1, arr2):
        return np.dot(arr1, arr2) / (np.linalg.norm(arr1) * np.linalg.norm(arr2))

    def correlation_coefficient(self, arr1, arr2):
        return np.corrcoef(arr1, arr2)[0, 1]

if __name__ == '__main__':
    comparer = ArrayComparer()
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])

    print("Euclidean Distance:", comparer.euclidean_distance(array1, array2))
    print("Cosine Similarity:", comparer.cosine_similarity(array1, array2))
    print("Correlation Coefficient:", comparer.correlation_coefficient(array1, array2))