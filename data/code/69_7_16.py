class SubListRetriever:
    def __init__(self, data):
        self._data = list(data)

    def get_sublist(self, start_index, end_index):
        if not isinstance(start_index, int) or not isinstance(end_index, int):
            raise TypeError("Start and end indices must be integers")
        if start_index < 0 or end_index >= len(self._data) or start_index > end_index:
            raise ValueError("Invalid start or end index")
        return self._data[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    retriever = SubListRetriever(sample_data)
    try:
        sublist = retriever.get_sublist(2, 5)
        print("Sublist from index 2 to 5:", sublist)
        sublist = retriever.get_sublist(0, 4)
        print("Sublist from index 0 to 4:", sublist)
        sublist = retriever.get_sublist(6, 9)
        print("Sublist from index 6 to 9:", sublist)
    except (TypeError, ValueError) as e:
        print(e)