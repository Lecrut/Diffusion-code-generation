import numpy as np

def find_smallest(data):
    return np.amax(np.negative(data))

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, -5, -20, -1]
    list3 = [0, 5, -10, 3]
    list4 = [7]
    list5 = [-5, 0, 5, -10]
    list6 = []
    
    print(f"Smallest in {list1}: {find_smallest(list1)}")
    print(f"Smallest in {list2}: {find_smallest(list2)}")
    print(f"Smallest in {list3}: {find_smallest(list3)}")
    print(f"Smallest in {list4}: {find_smallest(list4)}")
    print(f"Smallest in {list5}: {find_smallest(list5)}")