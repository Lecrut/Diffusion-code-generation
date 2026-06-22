import numpy as np

def find_max_value(lst):
    return np.max(lst)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_max_value(sample_list))