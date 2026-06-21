import numpy as np

class SmallestValueFinder:
    @staticmethod
    def find_smallest(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return np.amin(data)

if __name__ == '__main__':
    finder = SmallestValueFinder()
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, -5, -20, -1]
    list3 = [0, 5, -10, 3]
    list4 = [7]
    list5 = [-5, 0, 5, -10]
    list6 = []
    
    print(f"Smallest in {list1}: {finder.find_smallest(list1)}")
    print(f"Smallest in {list2}: {finder.find_smallest(list2)}")
    print(f"Smallest in {list3}: {finder.find_smallest(list3)}")
    print(f"Smallest in {list4}: {finder.find_smallest(list4)}")
    print(f"Smallest in {list5}: {finder.find_smallest(list5)}")