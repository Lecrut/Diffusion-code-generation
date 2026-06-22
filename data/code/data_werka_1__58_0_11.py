class SafeListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def first_element(self):
        if not self.data_list:
            raise IndexError("The list is empty.")
        return self.data_list[0]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20]
    accessor = SafeListAccessor(sample_data)
    try:
        print(accessor.first_element())
    except IndexError as e:
        print(e)