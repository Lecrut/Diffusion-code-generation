import numpy as np

def find_max_value(lst):
    return np.max(lst)

if __name__ == '__main__':
    sample_list = [34, 56, 23, 89, 12, 78]
    print(find_max_value(sample_list))