from functools import reduce

class MaxFinder:

    @staticmethod
    def compare(x, y):
        return x if x > y else y

    @classmethod
    def find_largest_element(cls, data):
        if not data:
            raise ValueError('Input list cannot be empty')
        return reduce(cls.compare, data)
if __name__ == '__main__':
    finder = MaxFinder()
    print(f'List 1: [10, 5, 20, 8, 15], Largest element: {finder.find_largest_element([10, 5, 20, 8, 15])}')
    print(f'List 2: [-5, -1, -10, -2], Largest element: {finder.find_largest_element([-5, -1, -10, -2])}')
    print(f'List 3: [7, 7, 7, 7], Largest element: {finder.find_largest_element([7, 7, 7, 7])}')
    print(f'List 4: [42], Largest element: {finder.find_largest_element([42])}')
    print(f'List 5: [-100, 0, -50], Largest element: {finder.find_largest_element([-100, 0, -50])}')