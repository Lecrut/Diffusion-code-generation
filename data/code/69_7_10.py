class SafeList:
    def __init__(self, data):
        self._data = list(data)

    def get_sublist(self, start_index, end_index):
        if not isinstance(start_index, int) or not isinstance(end_index, int):
            raise TypeError("Start and end indices must be integers")
        if start_index < 0 or end_index >= len(self._data) or start_index > end_index:
            raise IndexError("Invalid start or end index")
        return self._data[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    slist = SafeList(sample_data)
    
    try:
        sublist = slist.get_sublist(1, 3)
        print("Sublist from index 1 to 3:", sublist)
    except (TypeError, IndexError) as e:
        print("Error:", e)

    try:
        sublist = slist.get_sublist(0, 4)
        print("Sublist from index 0 to 4:", sublist)
    except (TypeError, IndexError) as e:
        print("Error:", e)

    try:
        sublist = slist.get_sublist(-1, 2)
        print("Sublist from index -1 to 2:", sublist)
    except (TypeError, IndexError) as e:
        print("Error:", e)

    try:
        sublist = slist.get_sublist(2, 5)
        print("Sublist from index 2 to 5:", sublist)
    except (TypeError, IndexError) as e:
        print("Error:", e)