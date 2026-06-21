class SubListRetriever:
    def __init__(self, data):
        self._data = list(data)

    def get_sublist(self, start_index, end_index):
        if not (isinstance(start_index, int) and isinstance(end_index, int)):
            raise TypeError("Start and end indices must be integers")
        if start_index < 0 or end_index >= len(self._data) or start_index > end_index:
            raise ValueError("Invalid start or end index")
        return self._data[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55]
    retriever = SubListRetriever(sample_data)
    
    start_index = 1
    end_index = 4
    print(f"Sub-list from index {start_index} to {end_index}: {retriever.get_sublist(start_index, end_index)}")
    
    try:
        invalid_start_index = 5
        print(f"Sub-list from index {invalid_start_index} to {end_index}: {retriever.get_sublist(invalid_start_index, end_index)}")
    except Exception as e:
        print(f"Error: {e}")