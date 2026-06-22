class MinFinder:
    MIN_VALUE = float('inf')

    @staticmethod
    def find_minimum(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        minimum = MinFinder.MIN_VALUE
        for x in data:
            if x < minimum:
                minimum = x
        return minimum

if __name__ == '__main__':
    finder = MinFinder()
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, 5, 0, -20, 100]
    list3 = [7]
    list4 = []
    print(f"Minimum of {list1}: {finder.find_minimum(list1)}")
    print(f"Minimum of {list2}: {finder.find_minimum(list2)}")
    print(f"Minimum of {list3}: {finder.find_minimum(list3)}")