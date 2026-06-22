class MinFinder:
    @staticmethod
    def find_min(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        minimum = data[0]
        for item in data[1:]:
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    min_finder = MinFinder()
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, -5, 3]
    list3 = [42]
    empty_list = []
    print(f"Minimum of {list1}: {min_finder.find_min(list1)}")
    print(f"Minimum of {list2}: {min_finder.find_min(list2)}")
    print(f"Minimum of {list3}: {min_finder.find_min(list3)}")
    try:
        min_finder.find_min(empty_list)
    except ValueError as e:
        print(e)