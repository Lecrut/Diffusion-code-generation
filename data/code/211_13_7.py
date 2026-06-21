import numpy as np

class ArrayMetrics:
    @staticmethod
    def euclidean_distance(arr1, arr2):
        return np.linalg.norm(arr1 - arr2)
    
    @staticmethod
    def cosine_similarity(arr1, arr2):
        dot_product = np.dot(arr1, arr2)
        norm_arr1 = np.linalg.norm(arr1)
        norm_arr2 = np.linalg.norm(arr2)
        return dot_product / (norm_arr1 * norm_arr2) if norm_arr1 * norm_arr2 != 0 else None
    
    @staticmethod
    def correlation_coefficient(arr1, arr2):
        return np.corrcoef(arr1, arr2)[0, 1]

if __name__ == '__main__':
    array_a = np.array([1, 2, 3])
    array_b = np.array([4, 5, 6])
    
    print("Euclidean Distance:", ArrayMetrics.euclidean_distance(array_a, array_b))
    print("Cosine Similarity:", ArrayMetrics.cosine_similarity(array_a, array_b))
    print("Correlation Coefficient:", ArrayMetrics.correlation_coefficient(array_a, array_b))