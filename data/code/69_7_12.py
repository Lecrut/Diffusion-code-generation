class ListSubslicer:
    def __init__(self, data):
        self._data = list(data)
    
    @staticmethod
    def get_sublist(data, start_index, end_index):
        if not isinstance(start_index, int) or not isinstance(end_index, int):
            raise TypeError("Indices must be integers")
        if start_index < 0 or end_index >= len(data):
            raise IndexError("Index out of range")
        return data[start_index:end_index + 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    slicer = ListSubslicer(sample_list)
    print(f"Sublist from index 1 to 3: {ListSubslicer.get_sublist(sample_list, 1, 3)}")