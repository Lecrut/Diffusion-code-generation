class ListHandler:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        return self.data[0] if self.data else None

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    handler = ListHandler(sample_list)
    first_value = handler.get_first_element()
    print(first_value)

    another_list = ['apple', 'banana', 'cherry']
    another_handler = ListHandler(another_list)
    first_fruit = another_handler.get_first_element()
    print(first_fruit)

    empty_list = []
    empty_handler = ListHandler(empty_list)
    first_empty = empty_handler.get_first_element()
    print(first_empty)