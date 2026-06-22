class ListWithMiddle:
    def __init__(self, data):
        self._data = list(data)
        self._length = len(self._data)
        self._middle_index = self._length // 2
        self._is_even_length = (self._length % 2 == 0)

    def get_middle(self):
        if self._length == 0:
            raise ValueError("List is empty")
        
        if self._is_even_length:
            return self._data[self._middle_index]
        else:
            return self._data[self._middle_index]

if __name__ == '__main__':
    sample_list = ListWithMiddle([10, 20, 30, 40, 50])
    print(sample_list.get_middle())
    
    sample_list_even = ListWithMiddle([10, 20, 30, 40])
    print(sample_list_even.get_middle())