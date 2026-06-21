class MaxFinder:
    @staticmethod
    def flatten(nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(MaxFinder.flatten(item))
            else:
                result.append(item)
        return result

    @staticmethod
    def find_max(flattened_list):
        return max(flattened_list)

if __name__ == '__main__':
    finder = MaxFinder()
    nested_list1 = [[1, 2, [3]], 4, [5, 6]]
    flattened_list1 = finder.flatten(nested_list1)
    result1 = finder.find_max(flattened_list1)
    print(f"Nested List: {nested_list1}, Flattened: {flattened_list1}, Max: {result1}")

    nested_list2 = [[10, [20, 30]], 40, [50, [60, 70]]]
    flattened_list2 = finder.flatten(nested_list2)
    result2 = finder.find_max(flattened_list2)
    print(f"Nested List: {nested_list2}, Flattened: {flattened_list2}, Max: {result2}")

    nested_list3 = [[-1, -2, [-3]], -4, [-5, -6]]
    flattened_list3 = finder.flatten(nested_list3)
    result3 = finder.find_max(flattened_list3)
    print(f"Nested List: {nested_list3}, Flattened: {flattened_list3}, Max: {result3}")