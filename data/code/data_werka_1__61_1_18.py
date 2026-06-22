class ListElementFetcher:
    LIST_TYPE = list
    INDEX_TYPE = int

    @staticmethod
    def validate_data(data):
        if not isinstance(data, ListElementFetcher.LIST_TYPE):
            raise TypeError("Input must be a list.")

    @staticmethod
    def validate_index(index):
        if not isinstance(index, ListElementFetcher.INDEX_TYPE):
            raise TypeError("Index must be an integer.")

    @staticmethod
    def get_element_at_position(data, index):
        ListElementFetcher.validate_data(data)
        ListElementFetcher.validate_index(index)
        if index < 0 or index >= len(data):
            raise IndexError("Index out of bounds.")
        return data[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    print(f"Original list: {sample_list}")
    try:
        result1 = ListElementFetcher.get_element_at_position(sample_list, 1)
        print(f"Element at index 1: {result1}")
        result2 = ListElementFetcher.get_element_at_position(sample_list, 3)
        print(f"Element at index 3: {result2}")
        result3 = ListElementFetcher.get_element_at_position(sample_list, 0)
        print(f"Element at index 0: {result3}")
    except Exception as e:
        print(f"An error occurred: {e}")