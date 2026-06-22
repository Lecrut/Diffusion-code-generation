import numpy as np

class MaxFinder:
    @staticmethod
    def find_maximum(data):
        if not data.size:
            raise ValueError("The array is empty")
        return np.max(data)

if __name__ == '__main__':
    sample_array1 = np.array([10, 5, 20, 8])
    sample_array2 = np.array([3, 99, 1, 42])
    
    max_value1 = MaxFinder.find_maximum(sample_array1)
    print(f"Maximum of {sample_array1}: {max_value1}")
    
    max_value2 = MaxFinder.find_maximum(sample_array2)
    print(f"Maximum of {sample_array2}: {max_value2}")