class NestedListMin:
    @staticmethod
    def flatten(data):
        result = []
        for item in data:
            if isinstance(item, list):
                result.extend(NestedListMin.flatten(item))
            else:
                result.append(item)
        return result

    @staticmethod
    def find_minimum(data):
        flat_list = NestedListMin.flatten(data)
        if not flat_list:
            raise ValueError("Input list cannot be empty")
        return min(flat_list)

if __name__ == '__main__':
    list1 = [5, 2, [8, 1]]
    list2 = []
    list3 = [-10, 0, [5]]

    try:
        result1 = NestedListMin.find_minimum(list1)
        print(f"Minimum of {list1}: {result1}")
        result3 = NestedListMin.find_minimum(list3)
        print(f"Minimum of {list3}: {result3}")
        NestedListMin.find_minimum(list2)
    except ValueError as e:
        print(f"Caught expected error for empty list: {e}")