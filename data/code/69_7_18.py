class SubListRetriever:
    def __init__(self, data):
        self._data = list(data)

    def get_sublist(self, start_index, end_index):
        if not (isinstance(start_index, int) and isinstance(end_index, int)):
            raise TypeError("Indices must be integers")
        if start_index < 0 or end_index >= len(self._data) or start_index > end_index:
            raise ValueError("Invalid index range")
        return self._data[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55]
    retriever = SubListRetriever(sample_data)
    
    start_idx = 1
    end_idx = 4
    sub_list = retriever.get_sublist(start_idx, end_idx)
    print(f"Sub-list from index {start_idx} to {end_idx}: {sub_list}")