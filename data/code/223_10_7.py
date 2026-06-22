class MaxFinder:
    def find_maximum(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return max(data)

if __name__ == '__main__':
    finder = MaxFinder()
    list1 = [1, 5, 2, 8, 3]
    list2 = [-10, -5, -20, -1]
    empty_list = []
    print(f"Maximum of {list1}: {finder.find_maximum(list1)}")
    print(f"Maximum of {list2}: {finder.find_maximum(list2)}")
    try:
        finder.find_maximum(empty_list)
    except ValueError as e:
        print(e)