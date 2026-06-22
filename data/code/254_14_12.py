def flatten_and_find_min(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_and_find_min(item))
        else:
            flat_list.append(item)
    return min(flat_list)

class NestedListMinFinder:
    def __init__(self, data):
        self.data = data

    def find_minimum(self):
        return flatten_and_find_min(self.data)

if __name__ == '__main__':
    list1 = [5, 2, [8, 1]]
    list2 = []
    list3 = [-10, 0, [5]]

    finder1 = NestedListMinFinder(list1)
    finder3 = NestedListMinFinder(list3)

    print(f"Minimum of {list1}: {finder1.find_minimum()}")
    print(f"Minimum of {list3}: {finder3.find_minimum()}")