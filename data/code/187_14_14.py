class ListProcessor:
    def __init__(self, data):
        self._data = data

    def get_largest_element(self):
        if not self._data:
            raise ValueError("Cannot find the largest element in an empty list.")
        return max(self._data)

if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 8]
    processor_one = ListProcessor(sample_list_one)
    try:
        largest_val_one = processor_one.get_largest_element()
        print(f"The largest element in {sample_list_one} is: {largest_val_one}")
    except ValueError as e:
        print(f"Error for sample list one: {e}")

    sample_list_two = [-5, -1, -10]
    processor_two = ListProcessor(sample_list_two)
    try:
        largest_val_two = processor_two.get_largest_element()
        print(f"The largest element in {sample_list_two} is: {largest_val_two}")
    except ValueError as e:
        print(f"Error for sample list two: {e}")