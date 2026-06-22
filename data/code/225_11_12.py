import numpy as np

class MinMaxFinder:
    @staticmethod
    def find_min_max(data: list) -> tuple:
        if not data:
            raise ValueError("Input list cannot be empty")
        return (np.min(data), np.max(data))

if __name__ == '__main__':
    finder = MinMaxFinder()
    list1 = [3, 1, 4, 1, 5, 9, 2, 6]
    result1 = finder.find_min_max(list1)
    print(f"List: {list1}, Min: {result1[0]}, Max: {result1[1]}")
    
    list2 = [-10, 5, 0, -20, 100]
    result2 = finder.find_min_max(list2)
    print(f"List: {list2}, Min: {result2[0]}, Max: {result2[1]}")