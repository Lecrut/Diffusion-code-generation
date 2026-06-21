class ListModifier:
    def __init__(self, data_list):
        self.data_list = data_list

    def remove_all_occurrences(self, item_to_remove):
        for i in range(len(self.data_list) - 1, -1, -1):
            if self.data_list[i] == item_to_remove:
                del self.data_list[i]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30]
    modifier = ListModifier(my_list)
    item_to_remove = 30
    print(f"Original list: {my_list}")
    modifier.remove_all_occurrences(item_to_remove)
    print(f"List after removing all occurrences of {item_to_remove}: {my_list}")