class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_second_item(self):
        if len(self.data_list) < 2:
            raise IndexError("List does not contain at least two items.")
        return self.data_list[1]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    accessor = ListAccessor(sample_list)
    try:
        second_item = accessor.get_second_item()
        print(second_item)
    except IndexError as e:
        print(e)