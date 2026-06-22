class ListManager:
    DEFAULT_LIST = [5, 10, 15, 20]

    def __init__(self, data=None):
        self.data = data if data is not None else ListManager.DEFAULT_LIST

    @classmethod
    def create_from_string(cls, string_data):
        return cls(string_data.split())

    def fetch_first_element(self):
        return self.data[0] if self.data else None

if __name__ == '__main__':
    sample_list = [100, 200, 300]
    manager = ListManager(sample_list)
    first_element = manager.fetch_first_element()
    print(first_element)

    string_manager = ListManager.create_from_string("one two three")
    first_element_from_string = string_manager.fetch_first_element()
    print(first_element_from_string)