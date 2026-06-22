def get_last_item(data):
    if not data:
        return None
    return data[-1]

class ListProcessor:
    def __init__(self, data):
        self.data = data

    def get_last(self):
        return get_last_item(self.data)

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = ['x', 'y', 'z']
    empty_list = []
    single_element_list = [900]

    processor_1 = ListProcessor(sample_list_1)
    processor_2 = ListProcessor(sample_list_2)
    processor_empty = ListProcessor(empty_list)
    processor_single = ListProcessor(single_element_list)

    print(processor_1.get_last())
    print(processor_2.get_last())
    print(processor_empty.get_last())
    print(processor_single.get_last())