class MinFinder:
    @staticmethod
    def find_smallest(data):
        if not data:
            return None
        smallest = data[0]
        for element in data[1:]:
            if element < smallest:
                smallest = element
        return smallest

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, -5, 3]
    list3 = [42]
    list4 = []
    print(f"Smallest in {list1}: {MinFinder.find_smallest(list1)}")
    print(f"Smallest in {list2}: {MinFinder.find_smallest(list2)}")
    print(f"Smallest in {list3}: {MinFinder.find_smallest(list3)}")
    print(f"Smallest in {list4}: {MinFinder.find_smallest(list4)}")