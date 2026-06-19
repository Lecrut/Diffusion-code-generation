class ListHandler:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        self.data = data

    def get_first_element(self):
        if not self.data:
            return None
        return self.data[0]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    handler = ListHandler(sample_list)
    first_value = handler.get_first_element()
    print(first_value)