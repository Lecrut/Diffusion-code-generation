class SafeListAccessor:
    def __init__(self, data):
        self.data = list(data)

    def get_element(self, index):
        if -len(self.data) <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45, 55]
    accessor = SafeListAccessor(sample_list)
    
    index_to_access = 3
    try:
        element = accessor.get_element(index_to_access)
        print(f"Element at index {index_to_access}: {element}")
    except IndexError as e:
        print(e)

    negative_index_to_access = -2
    try:
        element = accessor.get_element(negative_index_to_access)
        print(f"Element at index {negative_index_to_access}: {element}")
    except IndexError as e:
        print(e)

    out_of_bounds_index = 10
    try:
        element = accessor.get_element(out_of_bounds_index)
        print(f"Element at index {out_of_bounds_index}: {element}")
    except IndexError as e:
        print(e)

    negative_out_of_bounds_index = -7
    try:
        element = accessor.get_element(negative_out_of_bounds_index)
        print(f"Element at index {negative_out_of_bounds_index}: {element}")
    except IndexError as e:
        print(e)