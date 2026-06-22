class ListManager:
    def __init__(self, list_data):
        self.list_data = list_data

    @classmethod
    def from_mapping(cls, data_map):
        return cls(list(data_map.values()))

    def retrieve_first(self):
        if self.list_data:
            return self.list_data[0]
        else:
            return None

if __name__ == '__main__':
    sample_dict = {'x': 100, 'y': 200, 'z': 300}
    manager = ListManager.from_mapping(sample_dict)
    first_element = manager.retrieve_first()
    print(first_element)