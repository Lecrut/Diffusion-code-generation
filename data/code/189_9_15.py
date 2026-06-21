class ListModifier:
    def __init__(self, initial_data):
        self.data = initial_data

    def remove_all_occurrences(self, item_to_remove):
        index = len(self.data) - 1
        while index >= 0:
            if self.data[index] == item_to_remove:
                del self.data[index]
            index -= 1

if __name__ == '__main__':
    my_list = [10, 20, 30, 40, 50, 30, 30]
    modifier = ListModifier(my_list)
    item_to_remove = 30
    print("Original list:", modifier.data)
    modifier.remove_all_occurrences(item_to_remove)
    print("Resulting list:", modifier.data)