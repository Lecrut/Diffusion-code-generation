class MinFinder:
    def get_smallest(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        smallest = data_list[0]
        for item in data_list[1:]:
            if item < smallest:
                smallest = item
        return smallest
if __name__ == '__main__':
    finder = MinFinder()
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 5, -3]
    list3 = [42]
    list4 = []
    print(f"Smallest in {list1}: {finder.get_smallest(list1)}")
    print(f"Smallest in {list2}: {finder.get_smallest(list2)}")
    print(f"Smallest in {list3}: {finder.get_smallest(list3)}")
    try:
        finder.get_smallest(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")