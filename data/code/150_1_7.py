class ListModifier:
    @staticmethod
    def remove_item(input_list, target_item):
        return list(filter(lambda item: item != target_item, input_list))

if __name__ == '__main__':
    modifier = ListModifier()
    sample_list1 = [1, 2, 3, 2, 4, 2, 5]
    target_item1 = 2
    result1 = modifier.remove_item(sample_list1, target_item1)
    print(f"Original list: {sample_list1}")
    print(f"Target item: {target_item1}")
    print(f"New list: {result1}")

    sample_list2 = ['a', 'b', 'c', 'a', 'd']
    target_item2 = 'a'
    result2 = modifier.remove_item(sample_list2, target_item2)
    print(f"Original list: {sample_list2}")
    print(f"Target item: {target_item2}")
    print(f"New list: {result2}")

    sample_list3 = [10, 20, 30, 40]
    target_item3 = 5
    result3 = modifier.remove_item(sample_list3, target_item3)
    print(f"Original list: {sample_list3}")
    print(f"Target item: {target_item3}")
    print(f"New list: {result3}")