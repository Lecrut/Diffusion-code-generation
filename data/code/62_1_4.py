class ListAccessor:
    def __init__(self, lst):
        self.lst = lst

    def get_second_item(self):
        if len(self.lst) < 2:
            raise IndexError("List does not have a second item.")
        return self.lst[1]

if __name__ == '__main__':
    sample_list = [3, 13, 23]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_second_item())
    except IndexError as e:
        print(e)