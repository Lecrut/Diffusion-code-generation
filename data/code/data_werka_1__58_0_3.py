class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_first_element(self):
        if not self.data_list:
            raise ValueError("The list is empty.")
        return self.data_list[0]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45]
    accessor = ListAccessor(sample_list)
    first_element = accessor.get_first_element()
    print(first_element)