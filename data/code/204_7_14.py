import numpy as np

def compute_median(data):
    return np.median(data)

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(compute_median(list1))
    list2 = [7, 8, 5, 6, 2, 3, 4, 1]
    print(compute_median(list2))