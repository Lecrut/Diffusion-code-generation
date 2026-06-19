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
    sample_list = [10, 20, 30, 40, 50]
    retriever = SubListRetriever(sample_list)
    
    print("Sublist from index 1 to 3:", retriever.get_sublist(1, 3))
    print("Sublist from index 0 to 2:", retriever.get_sublist(0, 2))
    print("Sublist from index 2 to 4:", retriever.get_sublist(2, 4))
    
    try:
        print("Sublist from index 5 to 7:", retriever.get_sublist(5, 7))
    except Exception as e:
        print(e)
    
    try:
        print("Sublist from index -1 to 3:", retriever.get_sublist(-1, 3))
    except Exception as e:
        print(e)