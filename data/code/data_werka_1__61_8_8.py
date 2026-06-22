class ListElementAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_element(self, index):
        if not (0 <= index < len(self.data_list)):
            raise IndexError("Index out of bounds")
        return self.data_list[index]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    target_index = 4
    accessor = ListElementAccessor(sample_data)
    try:
        element = accessor.get_element(target_index)
        print(element)
    except IndexError as e:
        print(f"Error: {e}")