import numpy as np

def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return np.min(data)

if __name__ == '__main__':
    sample_list1 = [5, 2, 8, 1, 9]
    sample_list2 = [-10, -5, -20, -1]
    sample_list3 = [0, 5, -10, 3]
    sample_list4 = [7]
    sample_list5 = [-5, 0, 5, -10]
    
    print(f"Smallest in {sample_list1}: {find_smallest(sample_list1)}")
    print(f"Smallest in {sample_list2}: {find_smallest(sample_list2)}")
    print(f"Smallest in {sample_list3}: {find_smallest(sample_list3)}")
    print(f"Smallest in {sample_list4}: {find_smallest(sample_list4)}")
    print(f"Smallest in {sample_list5}: {find_smallest(sample_list5)}")