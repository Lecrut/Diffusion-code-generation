class ListAccessor:
    MIN_INDEX = 0

    @staticmethod
    def validate_index(data, index):
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < ListAccessor.MIN_INDEX or index >= len(data):
            raise IndexError("Index out of bounds.")

    @staticmethod
    def get_element_at_position(data, index):
        ListAccessor.validate_index(data, index)
        return data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"Original list: {sample_list}")
    try:
        result1 = ListAccessor.get_element_at_position(sample_list, 2)
        print(f"Element at index 2: {result1}")
        result2 = ListAccessor.get_element_at_position(sample_list, 0)
        print(f"Element at index 0: {result2}")
        result3 = ListAccessor.get_element_at_position(sample_list, 4)
        print(f"Element at index 4: {result3}")
    except Exception as e:
        print(f"An error occurred: {e}")