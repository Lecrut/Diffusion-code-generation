def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]

class ListHandler:
    def __init__(self, data):
        self.data = data

    def fetch_second_item(self):
        return get_second_item(self.data)

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = ['x', 'y']
    sample_list_3 = [42]

    handler_1 = ListHandler(sample_list_1)
    handler_2 = ListHandler(sample_list_2)
    handler_3 = ListHandler(sample_list_3)

    print(handler_1.fetch_second_item())
    print(handler_2.fetch_second_item())
    print(handler_3.fetch_second_item())