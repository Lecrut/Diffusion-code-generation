class FloatMaxFinder:
    def find_max(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        max_val = data[0]
        for x in data[1:]:
            if x > max_val:
                max_val = x
        return max_val
if __name__ == '__main__':
    finder = FloatMaxFinder()
    list1 = [3.14, 1.618, 2.718, 0.577]
    list2 = [-10.5, -5.2, -20.1, -1.0]
    list3 = [42.0]
    list4 = []
    print(f"Max of {list1}: {finder.find_max(list1)}")
    print(f"Max of {list2}: {finder.find_max(list2)}")
    print(f"Max of {list3}: {finder.find_max(list3)}")
    try:
        finder.find_max(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")