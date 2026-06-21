import numpy as np

def compute_median(data):
    return np.median(data)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(compute_median(list1))
    
    list2 = [10, 20, 30, 40, 50, 60]
    print(compute_median(list2))
    
    list3 = [7]
    print(compute_median(list3))
    
    list4 = []
    print(compute_median(list4))