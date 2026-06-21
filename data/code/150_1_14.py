class ListModifier:
    def __init__(self, input_list):
        self.input_list = input_list

    def remove_item(self, target_item):
        return [item for item in self.input_list if item != target_item]

if __name__ == '__main__':
    modifier1 = ListModifier([1, 2, 3, 2, 4, 2, 5])
    removed_target1 = 2
    result1 = modifier1.remove_item(removed_target1)
    print(f"Original list: {modifier1.input_list}")
    print(f"Target item: {removed_target1}")
    print(f"New list: {result1}")

    modifier2 = ListModifier(['a', 'b', 'c', 'a', 'd'])
    removed_target2 = 'a'
    result2 = modifier2.remove_item(removed_target2)
    print(f"Original list: {modifier2.input_list}")
    print(f"Target item: {removed_target2}")
    print(f"New list: {result2}")

    modifier3 = ListModifier([10, 20, 30, 40])
    removed_target3 = 5
    result3 = modifier3.remove_item(removed_target3)
    print(f"Original list: {modifier3.input_list}")
    print(f"Target item: {removed_target3}")
    print(f"New list: {result3}")