class ListAccessor:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def get_last_element(lst):
        return lst[-1]

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    accessor = ListAccessor(sample_list)
    last_element = ListAccessor.get_last_element(accessor.data)
    print(last_element)