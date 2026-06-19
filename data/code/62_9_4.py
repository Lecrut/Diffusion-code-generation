def access_second_item_directly(lst):
    return lst[1]

class Accessor:

    def __init__(self, items):
        self.items = items

    def get_second_item(self):
        if len(self.items) > 1:
            return self.items[1]
        else:
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    second_item_direct = access_second_item_directly(sample_list)
    print('Second item using direct indexing:', second_item_direct)
    accessor_instance = Accessor(sample_list)
    second_item_method = accessor_instance.get_second_item()
    print('Second item using class method:', second_item_method)