class MaxFinder:
    @staticmethod
    def find_maximum(data):
        if not data:
            raise ValueError("Input iterable cannot be empty")
        if isinstance(data[0], list):
            return max(MaxFinder.find_maximum(sublist) for sublist in data)
        return max(data)

if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.577]
    list2 = [-10.5, -5.2, -20.1]
    nested_list = [[1, 2], [3, 4], [5, [6, 7]]]
    empty_list = []
    try:
        max1 = MaxFinder.find_maximum(list1)
        print(f"Maximum of {list1}: {max1}")
        max2 = MaxFinder.find_maximum(list2)
        print(f"Maximum of {list2}: {max2}")
        max3 = MaxFinder.find_maximum(nested_list)
        print(f"Maximum of {nested_list}: {max3}")
        find_maximum(empty_list)
    except ValueError as e:
        print(e)