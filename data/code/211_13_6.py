import numpy as np

class ArrayComparator:
    def euclidean_distance(self, arr1, arr2):
        return np.linalg.norm(arr1 - arr2)

    def cosine_similarity(self, arr1, arr2):
        dot_product = np.dot(arr1, arr2)
        norm_arr1 = np.linalg.norm(arr1)
        norm_arr2 = np.linalg.norm(arr2)
        return dot_product / (norm_arr1 * norm_arr2)

    def correlation_coefficient(self, arr1, arr2):
        cov_matrix = np.cov(arr1, arr2)
        std_dev_arr1 = np.std(arr1)
        std_dev_arr2 = np.std(arr2)
        return cov_matrix[0, 1] / (std_dev_arr1 * std_dev_arr2)

if __name__ == '__main__':
    comparator = ArrayComparator()
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    print("Euclidean Distance:", comparator.euclidean_distance(arr1, arr2))
    print("Cosine Similarity:", comparator.cosine_similarity(arr1, arr2))
    print("Correlation Coefficient:", comparator.correlation_coefficient(arr1, arr2))