import numpy as np

def calculate_median(data):
    return np.median(data)

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Median of sample_list1:", calculate_median(sample_list1))
    
    sample_list2 = [0.5, 0.75, 1.25, 1.5, 2.0]
    print("Median of sample_list2:", calculate_median(sample_list2))