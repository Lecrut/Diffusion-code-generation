import numpy as np

class ArrayComparator:
    def __init__(self, array1, array2):
        self.array1 = np.array(array1)
        self.array2 = np.array(array2)

    def validate_arrays(self):
        if not isinstance(self.array1, np.ndarray) or not isinstance(self.array2, np.ndarray):
            raise ValueError("Both inputs must be NumPy arrays.")
        if self.array1.shape != self.array2.shape:
            raise ValueError("Arrays must have the same shape.")

    def euclidean_distance(self):
        self.validate_arrays()
        return np.linalg.norm(self.array1 - self.array2)

    def cosine_similarity(self):
        self.validate_arrays()
        dot_product = np.dot(self.array1, self.array2)
        norm1 = np.linalg.norm(self.array1)
        norm2 = np.linalg.norm(self.array2)
        return dot_product / (norm1 * norm2)

    def correlation_coefficient(self):
        self.validate_arrays()
        return np.corrcoef(self.array1, self.array2)[0, 1]

if __name__ == '__main__':
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    comparator = ArrayComparator(array1, array2)
    
    print("Euclidean Distance:", comparator.euclidean_distance())
    print("Cosine Similarity:", comparator.cosine_similarity())
    print("Correlation Coefficient:", comparator.correlation_coefficient())