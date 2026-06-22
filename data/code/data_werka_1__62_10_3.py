def get_second_item(lst):
    try:
        return lst[1]
    except IndexError:
        return None

class ListProcessor:
    def __init__(self, data):
        self.data = data

    def second_item(self):
        return get_second_item(self.data)

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = [5]
    processor_1 = ListProcessor(sample_list_1)
    processor_2 = ListProcessor(sample_list_2)
    print(processor_1.second_item())
    print(processor_2.second_item())