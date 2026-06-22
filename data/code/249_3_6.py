class LargestIntegerFinder:
    @staticmethod
    def find_largest(data):
        return max(data) if data else None

if __name__ == '__main__':
    finder = LargestIntegerFinder()
    list1 = [1, 5, 2, 8, 3]
    list2 = [-10, -5, -20]
    list3 = [42]
    empty_list = []
    
    print(f"Largest in {list1}: {finder.find_largest(list1)}")
    print(f"Largest in {list2}: {finder.find_largest(list2)}")
    print(f"Largest in {list3}: {finder.find_largest(list3)}")
    print(f"Largest in empty list: {finder.find_largest(empty_list)}")