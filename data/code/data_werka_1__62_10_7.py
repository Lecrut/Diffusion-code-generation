def get_second_item(lst):
    try:
        return lst[1]
    except IndexError:
        return None

class ListHandler:
    def __init__(self, data):
        self.data = data
    
    def fetch_second(self):
        return get_second_item(self.data)

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [5]
    handler_1 = ListHandler(sample_list_1)
    handler_2 = ListHandler(sample_list_2)
    
    print(handler_1.fetch_second())
    print(handler_2.fetch_second())