import numpy as np

def find_middle(data):
    return np.median(data)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(find_middle(list1))
    list2 = [10, 20, 30, 40, 50, 60]
    print(find_middle(list2))
    list3 = [7]
    print(find_middle(list3))
    list4 = []
    print(find_middle(list4))