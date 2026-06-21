from functools import reduce

class MaxFinder:
    @staticmethod
    def find_largest(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return reduce(lambda x, y: x if x > y else y, data)

if __name__ == '__main__':
    finder = MaxFinder()
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -2]
    list3 = [7, 7, 7, 7]
    list4 = [42]
    list5 = [-100, 0, -50]
    empty_list = []
    print(f"List 1: {list1}, Largest element: {finder.find_largest(list1)}")
    print(f"List 2: {list2}, Largest element: {finder.find_largest(list2)}")
    print(f"List 3: {list3}, Largest element: {finder.find_largest(list3)}")