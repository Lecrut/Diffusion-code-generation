class ListHandler:
    def __init__(self, data):
        self.data = data

    def get_last_element(self):
        if not self.data:
            return None
        return self.data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    handler = ListHandler(sample_list)
    last_element = handler.get_last_element()
    print(last_element)