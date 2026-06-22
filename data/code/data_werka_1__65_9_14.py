class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get(self, index):
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError("Position out of bounds")

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    accessor = ListAccessor(sample_data)
    
    try:
        target_index = 3
        element = accessor.get(target_index)
        print(f"Element at index {target_index}: {element}")
    except IndexError as e:
        print(e)