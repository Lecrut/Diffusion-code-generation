import numpy as np

class ArrayComparator:
    def __init__(self, array1, array2):
        self.array1 = np.array(array1)
        self.array2 = np.array(array2)

    def euclidean_distance(self):
        return np.linalg.norm(self.array1 - self.array2)

    def cosine_similarity(self):
        dot_product = np.dot(self.array1, self.array2)
        norm1 = np.linalg.norm(self.array1)
        norm2 = np.linalg.norm(self.array2)
        return dot_product / (norm1 * norm2) if norm1 > 0 and norm2 > 0 else 0

    def correlation_coefficient(self):
        cov_matrix = np.cov(self.array1, self.array2)
        std_dev1 = np.sqrt(cov_matrix[0, 0])
        std_dev2 = np.sqrt(cov_matrix[1, 1])
        return cov_matrix[0, 1] / (std_dev1 * std_dev2) if std_dev1 > 0 and std_dev2 > 0 else 0

if __name__ == '__main__':
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    comparator = ArrayComparator(array1, array2)
    print("Euclidean Distance:", comparator.euclidean_distance())
    print("Cosine Similarity:", comparator.cosine_similarity())
    print("Correlation Coefficient:", comparator.correlation_coefficient())