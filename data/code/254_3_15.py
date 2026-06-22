class MinFinder:
    @staticmethod
    def find_min(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        minimum = data[0]
        for element in data[1:]:
            if element < minimum:
                minimum = element
        return minimum

if __name__ == '__main__':
    finder = MinFinder()
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 5, -3]
    list3 = [42]
    print(f"Minimum of {list1}: {finder.find_min(list1)}")
    print(f"Minimum of {list2}: {finder.find_min(list2)}")
    print(f"Minimum of {list3}: {finder.find_min(list3)}")