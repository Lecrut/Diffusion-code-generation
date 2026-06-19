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
        index_to_retrieve = 3
        result = accessor.get(index_to_retrieve)
        print(f"Element at index {index_to_retrieve}: {result}")
    except IndexError as e:
        print(f"Error: {e}")

    try:
        out_of_bounds_index = 10
        result_out_of_bounds = accessor.get(out_of_bounds_index)
        print(f"Element at index {out_of_bounds_index}: {result_out_of_bounds}")
    except IndexError as e:
        print(f"Error: {e}")