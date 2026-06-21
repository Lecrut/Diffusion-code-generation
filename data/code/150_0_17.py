class ListProcessor:
    @staticmethod
    def remove_item(input_list, item_value):
        return [item for item in input_list if item != item_value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5]
    item_to_remove = 2
    result = ListProcessor.remove_item(sample_list, item_to_remove)
    print(result)