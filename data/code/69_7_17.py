class SubListRetriever:
    def __init__(self, data):
        self._data = list(data)

    def get_sublist(self, start_index, end_index):
        if not (isinstance(start_index, int) and isinstance(end_index, int)):
            raise TypeError("Start and end indices must be integers")
        if start_index < 0 or end_index >= len(self._data) or start_index > end_index:
            raise IndexError("Invalid start or end index")
        return self._data[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55]
    retriever = SubListRetriever(sample_data)
    print(f"Sublist from index 1 to 3: {retriever.get_sublist(1, 3)}")
    print(f"Sublist from index 0 to 2: {retriever.get_sublist(0, 2)}")
    print(f"Sublist from index 4 to 5: {retriever.get_sublist(4, 5)}")
    try:
        print(f"Sublist from index 6 to 7: {retriever.get_sublist(6, 7)}")
    except IndexError as e:
        print(e)