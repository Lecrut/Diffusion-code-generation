class ListModifier:
    def __init__(self, lst):
        self.lst = lst

    def remove_item(self, item_to_remove):
        if item_to_remove in self.lst:
            self.lst.remove(item_to_remove)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item_to_remove = 3
    modifier = ListModifier(sample_list)
    modifier.remove_item(item_to_remove)
    print(modifier.lst)