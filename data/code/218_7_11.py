class MinFinder:
    @staticmethod
    def find_minimum(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return data[0]

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = []
    list3 = [-10, -5, -20]
    try:
        result1 = MinFinder.find_minimum(list1)
        print(f"Minimum of {list1}: {result1}")
        result3 = MinFinder.find_minimum(list3)
        print(f"Minimum of {list3}: {result3}")
        MinFinder.find_minimum(list2)
    except ValueError as e:
        print(e)