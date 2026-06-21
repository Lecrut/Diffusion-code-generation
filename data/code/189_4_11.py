class ListProcessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def remove_item(self, item_to_remove):
        while item_to_remove in self.data_list:
            self.data_list.remove(item_to_remove)
        return self.data_list

if __name__ == '__main__':
    processor1 = ListProcessor([1, 2, 3, 4, 5])
    item_to_remove1 = 3
    result1 = processor1.remove_item(item_to_remove1)
    print(result1)

    processor2 = ListProcessor(['a', 'b', 'c', 'd', 'e'])
    item_to_remove2 = 'c'
    result2 = processor2.remove_item(item_to_remove2)
    print(result2)

    processor3 = ListProcessor([10, 20, 30])
    item_to_remove3 = 5
    result3 = processor3.remove_item(item_to_remove3)
    print(result3)