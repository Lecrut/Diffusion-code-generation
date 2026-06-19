class ListManager:
    def __init__(self, data_list):
        self.data_list = data_list

    @classmethod
    def from_tuple(cls, tuple_data):
        return cls(list(tuple_data))

    def get_first_element(self):
        if self.data_list:
            return self.data_list[0]
        return None

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35]
    manager = ListManager(sample_data)
    print(manager.get_first_element())

    tuple_data = (100, 200, 300)
    tuple_manager = ListManager.from_tuple(tuple_data)
    print(tuple_manager.get_first_element())