import numpy as np

class ArrayComparator:
    def __init__(self, array1, array2):
        if not isinstance(array1, np.ndarray) or not isinstance(array2, np.ndarray):
            raise ValueError("Both inputs must be NumPy arrays.")
        self.array1 = array1
        self.array2 = array2
    
    def euclidean_distance(self):
        return np.linalg.norm(self.array1 - self.array2)
    
    def cosine_similarity(self):
        dot_product = np.dot(self.array1, self.array2)
        norm1 = np.linalg.norm(self.array1)
        norm2 = np.linalg.norm(self.array2)
        if norm1 == 0 or norm2 == 0:
            raise ValueError("One of the arrays has a zero norm.")
        return dot_product / (norm1 * norm2)
    
    def correlation_coefficient(self):
        if self.array1.shape[0] != self.array2.shape[0]:
            raise ValueError("Arrays must have the same length for correlation coefficient calculation.")
        return np.corrcoef(self.array1, self.array2)[0, 1]

if __name__ == '__main__':
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    comparator = ArrayComparator(array1, array2)
    
    print("Euclidean Distance:", comparator.euclidean_distance())
    print("Cosine Similarity:", comparator.cosine_similarity())
    print("Correlation Coefficient:", comparator.correlation_coefficient())