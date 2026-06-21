class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_positive_index(self, index):
        if index < 0 or index >= len(self.data_list):
            raise IndexError("Index out of bounds for positive access")
        return self.data_list[index]

    def get_negative_index(self, index):
        if index >= 0 or abs(index) > len(self.data_list):
            raise IndexError("Index out of bounds for negative access")
        return self.data_list[index]

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    accessor = ListAccessor(sample_data)

    try:
        positive_element = accessor.get_positive_index(2)
        print(f"Element at positive index 2: {positive_element}")
    except IndexError as e:
        print(e)

    try:
        negative_element = accessor.get_negative_index(-1)
        print(f"Element at negative index -1: {negative_element}")
    except IndexError as e:
        print(e)

    try:
        out_of_bounds_positive = accessor.get_positive_index(5)
    except IndexError as e:
        print(f"Caught expected error for positive index: {e}")

    try:
        out_of_bounds_negative = accessor.get_negative_index(-6)
    except IndexError as e:
        print(f"Caught expected error for negative index: {e}")