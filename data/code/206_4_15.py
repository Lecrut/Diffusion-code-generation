class MinFinder:
    def find_smallest(self, data):
        if not data:
            return None
        return min(data)

if __name__ == '__main__':
    finder = MinFinder()
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 50, 3, 100, -5]
    list3 = [42]
    list4 = []
    print(f"Smallest in {list1}: {finder.find_smallest(list1)}")
    print(f"Smallest in {list2}: {finder.find_smallest(list2)}")
    print(f"Smallest in {list3}: {finder.find_smallest(list3)}")
    print(f"Smallest in {list4}: {finder.find_smallest(list4)}")