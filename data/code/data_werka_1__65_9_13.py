class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get(self, index):
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError("Position out of bounds")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    target_index = 2
    try:
        result = accessor.get(target_index)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")