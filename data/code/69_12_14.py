class ElementFetcher:
    def __init__(self, data_list):
        self.data_list = data_list

    def fetch_positive_index(self, index):
        if not (0 <= index < len(self.data_list)):
            raise IndexError("Index out of bounds for positive access")
        return self.data_list[index]

    def fetch_negative_index(self, index):
        if not (-len(self.data_list) <= index < 0):
            raise IndexError("Index out of bounds for negative access")
        return self.data_list[index]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55]
    fetcher = ElementFetcher(sample_data)

    try:
        positive_index_result = fetcher.fetch_positive_index(2)
        print(f"Element at positive index 2: {positive_index_result}")
    except IndexError as e:
        print(e)

    try:
        negative_index_result = fetcher.fetch_negative_index(-1)
        print(f"Element at negative index -1: {negative_index_result}")
    except IndexError as e:
        print(e)

    try:
        out_of_bounds_positive = fetcher.fetch_positive_index(6)
    except IndexError as e:
        print(f"Caught expected error for positive index out of bounds: {e}")

    try:
        out_of_bounds_negative = fetcher.fetch_negative_index(-7)
    except IndexError as e:
        print(f"Caught expected error for negative index out of bounds: {e}")