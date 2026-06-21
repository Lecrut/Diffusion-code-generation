class ListModifier:
    @staticmethod
    def remove_item(input_list, target_item):
        return list(filter(lambda item: item != target_item, input_list))

if __name__ == '__main__':
    modifier = ListModifier()
    sample_list = [1, 2, 3, 4, 5]
    element_to_remove = 3
    result = modifier.remove_item(sample_list, element_to_remove)
    print(result)