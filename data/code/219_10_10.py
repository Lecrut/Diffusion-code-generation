class MaxFinder:
    @staticmethod
    def find_max(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return max(data)

if __name__ == '__main__':
    finder = MaxFinder()
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -8, -2]
    list3 = [7]
    list4 = []
    
    print(f"Max of {list1}: {finder.find_max(list1)}")
    print(f"Max of {list2}: {finder.find_max(list2)}")
    print(f"Max of {list3}: {finder.find_max(list3)}")