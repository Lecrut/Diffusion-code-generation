class ListModifier:
    def __init__(self, data_list):
        self.data_list = data_list

    def remove_all_occurrences(self, item_to_remove):
        index = len(self.data_list) - 1
        while index >= 0:
            if self.data_list[index] == item_to_remove:
                del self.data_list[index]
            index -= 1

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30, 60]
    modifier = ListModifier(my_list)
    item_to_remove = 30
    print("Original list:", modifier.data_list)
    modifier.remove_all_occurrences(item_to_remove)
    print("\nModified list after removing all occurrences of", item_to_remove, ":", modifier.data_list)