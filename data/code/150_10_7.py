class ListModifier:
    def __init__(self, lst):
        self.lst = lst

    def remove_element(self, item_to_remove):
        if item_to_remove in self.lst:
            self.lst = [item for item in self.lst if item != item_to_remove]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    modifier = ListModifier(sample_list)
    modifier.remove_element(3)
    print(modifier.lst)