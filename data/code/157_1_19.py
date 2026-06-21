class SmallestElementFinder:
    @staticmethod
    def find_smallest(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return sorted(data)[0]

if __name__ == '__main__':
    finder = SmallestElementFinder()
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, 0, 5, -20, 3]
    list3 = [7]
    empty_list = []
    print(f"Smallest in {list1}: {finder.find_smallest(list1)}")
    print(f"Smallest in {list2}: {finder.find_smallest(list2)}")
    print(f"Smallest in {list3}: {finder.find_smallest(list3)}")
    try:
        finder.find_smallest(empty_list)
    except ValueError as e:
        print(e)