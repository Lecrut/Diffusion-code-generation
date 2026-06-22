class ElementFetcher:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        self.data = data

    def fetch(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    sample_list = [500, 600, 700, 800, 900]
    fetcher = ElementFetcher(sample_list)
    try:
        index_to_find = 3
        element = fetcher.fetch(index_to_find)
        print(f"Element at index {index_to_find}: {element}")
    except (TypeError, IndexError) as e:
        print(e)