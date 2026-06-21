import numpy as np

def compute_median(data):
    if not data:
        return None
    return np.median(data)

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"Median of {sample1}: {compute_median(sample1)}")
    
    sample2 = [10, 20, 30, 40, 50]
    print(f"Median of {sample2}: {compute_median(sample2)}")
    
    sample3 = []
    print(f"Median of {sample3}: {compute_median(sample3)}")