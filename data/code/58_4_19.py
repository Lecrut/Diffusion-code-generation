class ListManager:
    DEFAULT_LIST = [100, 200, 300, 400]

    def __init__(self, data=None):
        self.data = data if data is not None else ListManager.DEFAULT_LIST

    @classmethod
    def from_tuple(cls, tuple_data):
        return cls(list(tuple_data))

    def get_initial_element(self):
        return self.data[0] if self.data else None

if __name__ == '__main__':
    sample_list_manager = ListManager([5, 15, 25, 35])
    print(sample_list_manager.get_initial_element())

    tuple_data = (10, 20, 30)
    tuple_list_manager = ListManager.from_tuple(tuple_data)
    print(tuple_list_manager.get_initial_element())