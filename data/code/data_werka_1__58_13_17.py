class ListHandler:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        try:
            return self.data[0]
        except IndexError:
            raise ValueError("The list is empty")

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    handler = ListHandler(sample_list)
    first_element = handler.get_first_element()
    print(first_element)