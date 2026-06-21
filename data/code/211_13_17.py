import numpy as np

class ArrayComparator:
    def euclidean_distance(self, arr1, arr2):
        return np.sqrt(np.sum((arr1 - arr2) ** 2))

    def cosine_similarity(self, arr1, arr2):
        dot_product = np.dot(arr1, arr2)
        norm_arr1 = np.linalg.norm(arr1)
        norm_arr2 = np.linalg.norm(arr2)
        return dot_product / (norm_arr1 * norm_arr2)

    def correlation_coefficient(self, arr1, arr2):
        return np.corrcoef(arr1, arr2)[0, 1]

if __name__ == '__main__':
    comparator = ArrayComparator()
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])

    print("Euclidean Distance:", comparator.euclidean_distance(array1, array2))
    print("Cosine Similarity:", comparator.cosine_similarity(array1, array2))
    print("Correlation Coefficient:", comparator.correlation_coefficient(array1, array2))