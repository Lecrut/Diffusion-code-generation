class SubListRetriever:
    def __init__(self, data):
        self._data = data

    def get_sublist(self, start_index, end_index):
        if not (0 <= start_index <= end_index < len(self._data)):
            raise IndexError("Start and end indices are out of bounds or invalid")
        return self._data[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55, 65]
    retriever = SubListRetriever(sample_data)
    start_idx = 2
    end_idx = 5
    sub_list = retriever.get_sublist(start_idx, end_idx)
    print(f"Sublist from index {start_idx} to {end_idx}: {sub_list}")