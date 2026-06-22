class ListAccessor:
    def __init__(self, data_list):
        self.data_list = data_list

    def get(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError("Position out of bounds")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    
    try:
        result = accessor.get(2)
        print(result)
    except (IndexError, TypeError) as e:
        print(f"Error: {e}")

    try:
        invalid_result = accessor.get(-1)
        print(invalid_result)
    except (IndexError, TypeError) as e:
        print(f"Error: {e}")

    try:
        non_integer_result = accessor.get("two")
        print(non_integer_result)
    except (IndexError, TypeError) as e:
        print(f"Error: {e}")